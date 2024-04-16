import numpy as np
import pandas as pd
import seaborn as sns
import os
import pickle
import gc
import decimal
import torch
import torch.nn as nn
from torch.optim.lr_scheduler import ExponentialLR
from torch.utils.data import Dataset, DataLoader

from tqdm import tqdm, tqdm_notebook
from matplotlib import pyplot as plt
import matplotlib.patches as patches
from matplotlib.font_manager import FontProperties
from sklearn.preprocessing import LabelEncoder
from sklearn.metrics import f1_score, confusion_matrix, classification_report


class _ShowAttributeNamesClass:
    """Service class for convenient access to protected attributes of NetworkWrapper"""
    n_classes = None
    num_workers = None
    batch_size = None
    best_model_wts = None
    accuracy_by_class = None
    is_metrics_updated = None
    relative_path = None
    label_encoder = None
    figsize = None
    graphics_location = None
    main_windows_path = None
    main_colab_path = None
    device = None

    def __init__(self, *args, **kwargs):
        self.__dict__ = kwargs

    def __setattr__(self, key, value):
        if key in self.__dict__:
            self.main_class.__dict__[f'_{key}'] = value
        return super().__setattr__(key, value)


class NetworkWrapper:
    _main_windows_path: str = None
    _main_colab_path: str = None

    def __init__(self, train_dataset, val_dataset, n_classes, model, relative_path, colab_view,
                 batch_size=None, epochs=None, lr=3e-4, scheduler_gamma=0.9, num_workers=0,
                 load_pretrained_model=True, save_best_weights=True, save_weights_by_epoch=True, label_encoder=None):
        self._is_windows = True if os.name == 'nt' else False
        self._separator = '\\' if self._is_windows else '/'
        self._main_path = self._main_windows_path if self._is_windows else self._main_colab_path
        if (self._is_windows and not self._main_windows_path) \
                or (not self._is_windows and not self._main_colab_path):
            print(
                f'The main part of the absolute path is set in the project launch directory: "{os.path.abspath(".")}"\n'
                f'You can explicitly specify the main part by calling '
                f'NetworkWrapper.set_main_paths({"main_windows_path" if self._is_windows else "main_colab_path"}=your_path)\n')
            self._main_path = os.path.abspath('.') + self._separator

        self.train_dataset = train_dataset
        self.val_dataset = val_dataset
        self._n_classes = n_classes

        self.model = model
        self.optimizer = torch.optim.Adam(model.parameters(), lr=lr)
        self.scheduler = ExponentialLR(self.optimizer, gamma=scheduler_gamma)
        self.criterion = nn.CrossEntropyLoss()

        self._batch_size = batch_size
        self._num_workers = num_workers
        self._total_epochs = epochs
        self._loaded_epoch = None

        self._load_pretrained_model = load_pretrained_model
        self._colab_view = colab_view
        self._figsize = (15, 9) if self._colab_view else (9, 6)
        self._graphics_location = (100, 50)
        self._tqdm = tqdm_notebook if self._colab_view else tqdm
        self._relative_path = relative_path
        self.full_path = self._main_path + self._relative_path
        os.makedirs(self._main_path + self._separator.join(relative_path.split(self._separator)[:-1]), exist_ok=True)

        self._device = torch.device("cuda" if torch.cuda.is_available() else 'cpu')
        self.model = self.model.to(self._device)
        self._save_best_weights = save_best_weights
        self.save_weights_by_epoch = save_weights_by_epoch
        self.best_epoch = -1  # range(0, self._total_epochs)
        self._y_preds = None
        self.actual_labels = None
        self.metrics = None
        self._is_metrics_updated = False
        self._accuracy_by_class = None
        self._best_model_wts = None
        self._protected_attributes = None
        self._requires_label_encoder = isinstance(self.train_dataset[0][1], str)
        if self._requires_label_encoder:
            print("Labels of type str detected, LabelEncoder required.\n")
        self._label_encoder = label_encoder
        if not isinstance(self._label_encoder, LabelEncoder) and self._requires_label_encoder:
            encoder_path = self._separator.join(self._main_path.split(self._separator)[:-1]) + self._separator + \
                           'Files' + self._separator + 'label_encoders'
            os.makedirs(encoder_path, exist_ok=True)
            filename = self._relative_path.split(self._separator)[-1]
            encoder_path_with_its_name = encoder_path + self._separator + filename + '_label_encoder.pkl'

            if isinstance(self._label_encoder, str):
                print(f'Loading LabelEncoder "{self._label_encoder.split(self._separator)[-1]}"...\n')
                self._label_encoder = self.load_label_encoder(self._main_path + self._label_encoder)
            elif os.path.isfile(encoder_path_with_its_name):
                self._label_encoder = self.load_label_encoder(encoder_path_with_its_name)
                print(f'Loaded LabelEncoder "{filename}_label_encoder.pkl"\n')
            else:
                print(f'Fitting LabelEncoder...\nP.s. This process may take a long time. '
                      f'You can pass a pre-trained LabelEncoder, path or list of labels to the "label_encoder" parameter of the initializer.\n')
                self._label_encoder = LabelEncoder().fit(np.unique([y for _, y in train_dataset]))
                with open(encoder_path_with_its_name, 'wb') as le_dump_file:
                    pickle.dump(self._label_encoder, le_dump_file)

    def train_load_model(self, calculate_metrics: bool = True) -> None:
        """
        A method that starts training (loading from a file) of a model. Always runs first.
        :param bool calculate_metrics: If True, automatically updates metrics.
        """
        gc.collect()
        torch.cuda.empty_cache()
        if not os.path.exists(self.full_path) or not self._load_pretrained_model:
            print("Start training model...")
            self._train()
        else:
            print(f"Loading pretrained model {self._relative_path.split(self._separator)[-1]}...")

        gc.collect()
        torch.cuda.empty_cache()
        state = torch.load(self.full_path, map_location='cpu')
        self.model.load_state_dict(state['best_model_weights'])
        self.optimizer.load_state_dict(state['optimizer_on_best_epoch'])
        self._history = state['history']
        self._total_epochs = state['total_epochs']
        self._loaded_epoch = self.best_epoch = state['best_epoch']
        if 'weights_by_epoch' in state:
            self._weights_by_epoch = state['weights_by_epoch']
        if calculate_metrics:
            self._update_metrics()
            self._is_metrics_updated = True

    def _train(self, start_epoch=0):
        if start_epoch not in range(0, self._total_epochs):
            raise ValueError(f"Epoch must be in range [0, {self._total_epochs - 1}]")

        train_loader = DataLoader(self.train_dataset, batch_size=self._batch_size,
                                  shuffle=True, num_workers=self._num_workers)
        val_loader = DataLoader(self.val_dataset, batch_size=self._batch_size,
                                shuffle=False, num_workers=self._num_workers)
        history = []
        if self.save_weights_by_epoch:
            weights_by_epoch_history = {'model': [], 'optimizer': []}
        log_template = "Epoch {ep:03d} \
        train_loss {t_loss:0.4f} val_loss {v_loss:0.4f} \
        train_acc {t_acc:0.4f} val_acc {v_acc:0.4f} \
        lr: {lr_dict}\n"
        best_acc = -1 if start_epoch == 0 else self._history['val_acc'][self.best_epoch]

        for epoch in (pbar_outer := self._tqdm(range(start_epoch, self._total_epochs), desc="Epoch",
                                               total=self._total_epochs - start_epoch,
                                               ncols=750 if self._colab_view else 75)):
            train_loss, train_acc = self._fit_epoch(train_loader)

            val_loss, val_acc = self._eval_epoch(val_loader)
            history.append((train_loss, train_acc, val_loss, val_acc))
            self.scheduler.step()

            if self.save_weights_by_epoch:
                temp_model_path = self._separator.join(self.full_path.split(self._separator)[:-1]) + \
                                  self._separator + 'temp.pth'
                torch.save(self.model.state_dict(), temp_model_path)
                weights_by_epoch_history['model'].append(torch.load(temp_model_path, map_location='cpu'))
                os.remove(temp_model_path)

                torch.save(self.optimizer.state_dict(), temp_model_path)
                weights_by_epoch_history['optimizer'].append(torch.load(temp_model_path, map_location='cpu'))
                os.remove(temp_model_path)

            if val_acc > best_acc:
                best_acc = val_acc
                self.best_epoch = epoch
                self._best_model_wts = self.model.state_dict()

            lr_dict = {f'lr{i + 1}': '%.2e' % decimal.Decimal(g['lr']) for i, g in
                       enumerate(self.optimizer.param_groups)}
            pbar_outer.write(log_template.format(ep=epoch, t_loss=train_loss, v_loss=val_loss,
                                                 t_acc=train_acc, v_acc=val_acc, lr_dict=lr_dict))
        self._loaded_epoch = self.best_epoch
        self._dump_state(history, start_epoch, weights_by_epoch_history)

    def _dump_state(self, history, start_epoch, weights_by_epoch_history=None):
        history_dict = {'train_loss': [], 'val_loss': [], 'train_acc': [], 'val_acc': []}
        if os.path.exists(self.full_path) and start_epoch > 0:
            state = torch.load(self.full_path, map_location='cpu')
            self.optimizer.load_state_dict(state['optimizer_on_best_epoch'])

            # Обрезаем эпохи, которые будем переобучать
            history_dict = {
                'train_loss': state['history']['train_loss'][:start_epoch],
                'val_loss': state['history']['val_loss'][:start_epoch],
                'train_acc': state['history']['train_acc'][:start_epoch],
                'val_acc': state['history']['val_acc'][:start_epoch]
            }

            if 'weights_by_epoch' in state:
                if weights_by_epoch_history is None:
                    weights_by_epoch_history = state['weights_by_epoch']
                else:
                    weights_by_epoch_history = {
                        'model': state['weights_by_epoch']['model'][:start_epoch] + weights_by_epoch_history['model'],
                        'optimizer': state['weights_by_epoch']['optimizer'][:start_epoch] + weights_by_epoch_history[
                            'optimizer']
                    }

        for train_loss, train_acc, val_loss, val_acc in history:
            history_dict['train_loss'].append(train_loss)
            history_dict['train_acc'].append(train_acc)
            history_dict['val_loss'].append(val_loss)
            history_dict['val_acc'].append(val_acc.item())

        # загрузим лучшие веса модели
        self.model.load_state_dict(self._best_model_wts)
        if self._save_best_weights:
            state = {
                'total_epochs': self._total_epochs,
                'best_epoch': self.best_epoch,
                'best_model_weights': self._best_model_wts,
                'optimizer_on_best_epoch': weights_by_epoch_history['optimizer'][self.best_epoch],
                'history': history_dict
            }
            if self.save_weights_by_epoch:
                state['weights_by_epoch'] = weights_by_epoch_history
            torch.save(state, getattr(self, '_retraining_path', self.full_path))

    def _fit_epoch(self, train_loader):
        running_loss = 0.0
        running_corrects = 0
        processed_data = 0
        self.model.train()

        for inputs, labels in self._tqdm(train_loader, colour='red',
                                         desc='Fit epoch', ncols=750 if self._colab_view else 75):
            inputs = inputs.float().to(self._device)
            if self._requires_label_encoder:
                labels = self._label_encoder.transform(labels)
            labels = torch.tensor(labels, dtype=torch.int64).to(self._device)

            outputs = self.model(inputs)
            loss = self.criterion(outputs, labels).mean()  # .mean() на случай, если у нас сегментация, у которой loss - это вектор
            self.optimizer.zero_grad()
            loss.backward()  # расчитать (вычислить) градиенты, не обновить
            self.optimizer.step()

            preds = torch.argmax(outputs, 1)  # выбираем класс с наибольшей вероятностью для каждого объекта батча
            running_loss += loss.item() * inputs.size(0)  # По умолчанию считается средний loss по батчу. Переводим его в суммарный loss, чтобы потом посчитать средний loss уже по эпохе
            running_corrects += torch.sum(preds == labels.data)
            processed_data += inputs.size(0)

        train_loss = running_loss / processed_data
        train_acc = running_corrects.cpu().numpy() / processed_data
        return train_loss, train_acc

    def _eval_epoch(self, val_loader):
        self.model.eval()
        running_loss = 0.0
        running_corrects = 0
        processed_size = 0
        for inputs, labels in self._tqdm(val_loader, colour='green',
                                         desc='Evaluate epoch', ncols=750 if self._colab_view else 75):
            inputs = inputs.to(self._device)
            if self._requires_label_encoder:
                labels = self._label_encoder.transform(labels)
            labels = torch.tensor(labels, dtype=torch.int64).to(self._device)

            with torch.set_grad_enabled(False):
                outputs = self.model(inputs)
                loss = self.criterion(outputs, labels)
                preds = torch.argmax(outputs, 1)

            running_loss += loss.item() * inputs.size(0)
            running_corrects += torch.sum(preds == labels.data)
            processed_size += inputs.size(0)
        val_loss = running_loss / processed_size
        val_acc = running_corrects.cpu().double() / processed_size

        return val_loss, val_acc

    def resume_model_training(self, start_epoch, total_epochs, relative_path=None):
        if total_epochs < 0:
            raise ValueError(f"End_epoch must be positive")
        self._total_epochs = total_epochs

        if relative_path is None:
            relative_path = self.full_path
        self._retraining_path = self._main_path + relative_path
        os.makedirs(self._main_path + self._separator.join(relative_path.split(self._separator)[:-1]), exist_ok=True)
        print(f"\nResume training model from epoch = {start_epoch} to total_epochs = {total_epochs}, not inclusive...")
        self._train(start_epoch=start_epoch)

        gc.collect()
        torch.cuda.empty_cache()
        state = torch.load(self._retraining_path, map_location='cpu')
        self.model.load_state_dict(state['best_model_weights'])
        self.optimizer.load_state_dict(state['optimizer_on_best_epoch'])
        self._history = state['history']
        self._total_epochs = state['total_epochs']
        self._loaded_epoch = self.best_epoch = state['best_epoch']
        if 'weights_by_epoch' in state:
            self._weights_by_epoch = state['weights_by_epoch']
        self._update_metrics()
        self._is_metrics_updated = True

    def predict(self, dataset, use_label_encoder=False):
        use_label_encoder = use_label_encoder and self._requires_label_encoder
        probs = self.predict_proba(dataset)
        y_preds = np.argmax(probs, -1)
        if use_label_encoder:
            y_preds = self._label_encoder.inverse_transform(y_preds)
        return y_preds

    def predict_proba(self, dataset):
        self.model.eval()

        if isinstance(dataset, type(DataLoader(Dataset()))):
            loader = iter(dataset)
        else:
            loader = iter(
                DataLoader(dataset, shuffle=False, batch_size=self._batch_size, num_workers=self._num_workers))

        logits = torch.empty((len(dataset), self._n_classes))
        if type(dataset[0]) == tuple:
            actual_labels = torch.empty(len(dataset), dtype=torch.int)

        with torch.no_grad():
            # P.s. Of course, we calculate logits, not probabilities
            for i, inputs in self._tqdm(enumerate(loader), colour='green', total=len(loader),
                                        desc='Calculate probabilities', ncols=750 if self._colab_view else 75):

                if type(inputs) != torch.tensor:
                    inputs, y = inputs
                    if self._requires_label_encoder:
                        y = self._label_encoder.transform(y)
                    y = torch.tensor(y).to(self._device)
                    actual_labels[i * self._batch_size: min((i + 1) * self._batch_size, len(dataset))] = y
                inputs = inputs.to(self._device)
                logits[i * self._batch_size: min((i + 1) * self._batch_size, len(dataset))] = self.model(inputs).cpu()

        self.actual_labels = actual_labels.numpy()
        probs = nn.functional.softmax(logits, dim=-1).detach().numpy()
        return probs

    def predict_one_sample(self, inputs, predict_proba=False, use_label_encoder=True):
        """Prediction for one image"""
        use_label_encoder = use_label_encoder and self._requires_label_encoder
        self.model.eval()
        with torch.no_grad():
            inputs = inputs.to(self._device)

            logit = self.model(inputs).cpu()
            probs = torch.nn.functional.softmax(logit, dim=-1).numpy()

        if predict_proba:
            return probs

        y_preds = np.argmax(probs, -1)
        if use_label_encoder:
            y_preds = self._label_encoder.inverse_transform(y_preds)
        return y_preds

    def plot_metrics(self, start_epoch=None, end_epoch=None, show_truncated_part=False):  # range(0, self._total_epochs)
        fig = plt.figure(figsize=self._figsize)
        fig.suptitle('Accuracy and loss of training/validation datasets by epoch', x=0.5, y=0.94)
        if not self._colab_view:
            x, y = self._graphics_location
            fig.canvas.manager.window.wm_geometry(f"+{x}+{y}")
        sns.set_style("whitegrid")

        total_epochs = max(self._total_epochs, show_truncated_part * (len(self._history['val_loss'])))
        if start_epoch is None:
            start_epoch = 0
        if end_epoch is None:
            end_epoch = self._total_epochs - 1 if self._loaded_epoch == self.best_epoch else self._loaded_epoch
        if start_epoch not in range(0, total_epochs) or end_epoch not in range(0, total_epochs):
            raise ValueError(f"Start and end epochs must be in range [0, {total_epochs - 1}]")

        plt.subplot(1, 2, 1)
        plt.xticks(ticks=list(range(start_epoch, end_epoch + 1)))
        plt.plot(self._history['train_loss'][start_epoch:end_epoch + 1], label="train_loss")
        plt.plot(self._history['val_loss'][start_epoch:end_epoch + 1], label="val_loss")
        plt.legend(loc='best')
        plt.xlabel("Epochs")
        plt.ylabel("Loss")

        plt.subplot(1, 2, 2)
        plt.xticks(ticks=list(range(start_epoch, end_epoch + 1)))
        plt.plot(self._history['train_acc'][start_epoch:end_epoch + 1], label="train_accuracy")
        plt.plot(self._history['val_acc'][start_epoch:end_epoch + 1], label="val_accuracy")
        plt.legend(loc='best')
        plt.xlabel("Epochs")
        plt.ylabel("Accuracy")

        plt.show()

    def plot_correct_class_prediction_hist(self, use_label_encoder=True, show_classes_proportions=True):
        use_label_encoder = use_label_encoder and self._requires_label_encoder
        fig, ax = plt.subplots(figsize=self._figsize)
        fig.suptitle('Class-wise accuracy on a validation dataset', x=0.5, y=0.94)
        plt.xticks(ticks=list(range(self._n_classes)),
                   labels=self._label_encoder.classes_ if use_label_encoder else list(self._accuracy_by_class.index),
                   size='small', rotation='vertical')
        plt.tight_layout()
        if not self._colab_view:
            x, y = self._graphics_location
            fig.canvas.manager.window.wm_geometry(f"+{x}+{y}")
        sns.set_style("whitegrid")

        if not self._is_metrics_updated or self._accuracy_by_class is None:
            self._update_accuracy_by_class_distribution()

        if use_label_encoder and not isinstance(list(self._accuracy_by_class.index)[0], str):
            self._accuracy_by_class.index = self._label_encoder.inverse_transform(self._accuracy_by_class.index)

        if show_classes_proportions:
            examples = self.get_metrics('stats_by_class')['examples']
            ratios = examples[:self._n_classes] / examples['micro avg']
            for index, (value, ratio) in enumerate(zip(self._accuracy_by_class.values, ratios)):
                ax.bar(index, value * ratio, color='red')
                ax.bar(index, value * (1 - ratio), bottom=value * ratio, color='blue')
        else:
            self._accuracy_by_class.plot(kind='bar')
        plt.show()

    def plot_confidence_on_examples(self, nrows=2, ncols=3, is_randomized=False):
        if not hasattr(self, '_plot_confidence_seed'):
            self._plot_confidence_seed = int(np.random.uniform(0, 10000))
        np.random.seed(None if is_randomized else self._plot_confidence_seed)

        fig, ax = plt.subplots(nrows=nrows, ncols=ncols, figsize=self._figsize, sharey=True, sharex=True)
        fig.suptitle('Confidences and actual labels for examples from val_dataset', x=0.5, y=0.97)
        if not self._colab_view:
            x, y = self._graphics_location
            fig.canvas.manager.window.wm_geometry(f"+{x}+{y}")

        axes = [ax] if nrows == ncols == 1 else ax.flatten()
        for fig_x in axes:
            fig_x.get_xaxis().set_visible(False)
            fig_x.get_yaxis().set_visible(False)

            random_character = int(np.random.uniform(0, len(self.val_dataset) - 1))
            im_val, label = self.val_dataset[random_character]
            if not isinstance(label, str) and self._requires_label_encoder:
                label = self._label_encoder.inverse_transform([label])[0]
            img_label = label if isinstance(label, int) else \
                " ".join(map(lambda x: x.capitalize(), label.split('_')))

            self.imshow(im_val.data.cpu().numpy(), title=img_label, plt_ax=fig_x)

            side_length = im_val.data.cpu().shape[-1]
            fig_x.add_patch(patches.Rectangle((0, 0.2366 * side_length), 0.3839 * side_length, 0.15625 * side_length,
                                              color='white'))
            font0 = FontProperties()
            font = font0.copy()
            font.set_family("fantasy")
            prob_pred = self.predict_one_sample(im_val.unsqueeze(0), use_label_encoder=False, predict_proba=True)
            predicted_proba = np.max(prob_pred) * 100
            y_pred = np.argmax(prob_pred)

            predicted_label = self._label_encoder.inverse_transform([y_pred])[0] \
                if self._requires_label_encoder else y_pred
            if isinstance(predicted_label, str):
                predicted_label = predicted_label[:len(predicted_label) // 2] + '\n' + \
                                  predicted_label[len(predicted_label) // 2:]
            predicted_text = "{} : {:.0f}%".format(predicted_label, predicted_proba)

            fig_x.text(side_length / 224, 0.241 * side_length, predicted_text, horizontalalignment='left',
                       fontproperties=font,
                       verticalalignment='top', fontsize=24 / (nrows * ncols + 1) ** 0.5, color='black',
                       fontweight='bold')

        plt.show()

    def get_encoded_actual_labels(self):
        if self._requires_label_encoder:
            return self._label_encoder.inverse_transform(self.actual_labels)
        return self.actual_labels

    def get_history(self, show_truncated_part=False):
        if show_truncated_part:
            return self._history
        else:
            return {key: value[:self._loaded_epoch + 1] for key, value in self._history.items()}

    def get_metrics(self, metrics=None):
        supported_metrics = ['accuracy', 'loss', 'f1-score', 'stats_by_class']
        if metrics is None:
            metrics = supported_metrics[:-1]
        if type(metrics) != list:
            metrics = [metrics]
        if not self._is_metrics_updated:
            self._update_metrics()

        for metric in metrics:
            if metric not in supported_metrics:
                raise KeyError(f"Metric {metric} not in supported_metrics ({supported_metrics}).")

        if len(metrics) == 1:
            return self.metrics[metrics[0]]
        return {key: value for key, value in self.metrics.items()
                if key in metrics}

    def _update_metrics(self, f1_score_average='weighted'):
        if f1_score_average not in ['micro', 'macro', 'weighted']:
            raise ValueError(
                "The f1_score_average parameter can take one of the following values: ['micro', 'macro', 'weighted']")
        self._y_preds = self.predict(self.val_dataset)

        metrics = {}
        metrics['accuracy'] = self._history['val_acc'][self._loaded_epoch]
        metrics['loss'] = self._history['val_loss'][self._loaded_epoch]
        metrics['f1-score'] = f1_score(self.actual_labels, self._y_preds, average=f1_score_average, zero_division=0)
        metrics['stats_by_class'] = self._get_stats_by_class()

        self._is_metrics_updated = True
        self.metrics = metrics

    def _get_stats_by_class(self, use_label_encoder=True):
        use_label_encoder = use_label_encoder and self._requires_label_encoder
        stats_by_class = pd.DataFrame(classification_report(self.actual_labels, self._y_preds,
                                                            zero_division=0, output_dict=True))
        stats_by_class.index = ['precision', 'recall', 'f1-score', 'examples']
        stats_by_class = stats_by_class.rename(columns={'accuracy': 'micro avg'})
        stats_by_class['micro avg'][3] = int(stats_by_class['macro avg'][3])
        stats_by_class = stats_by_class.T
        stats_by_class['examples'] = stats_by_class['examples'].astype('int')

        self._update_accuracy_by_class_distribution()
        stats_by_class['accuracy'] = 0
        percent_per_class = 100 * stats_by_class['examples'][:self._n_classes] / stats_by_class['examples'][-1]
        stats_by_class = stats_by_class[['accuracy', 'precision', 'recall', 'f1-score', 'examples']]
        stats_by_class['accuracy'][:self._n_classes] = self._accuracy_by_class
        stats_by_class['accuracy']['micro avg'] = stats_by_class['precision'][-3]
        stats_by_class['accuracy']['macro avg'] = stats_by_class.iloc[:self._n_classes, 0].mean()
        stats_by_class['accuracy']['weighted avg'] = (
                    stats_by_class['accuracy'][:self._n_classes] * percent_per_class / 100).sum()
        stats_by_class['percent'] = percent_per_class.round(2).astype('str') + '%'

        if use_label_encoder:
            transformed_indexes = list(map(int, list(stats_by_class.index)[:-3]))
            stats_by_class.index = list(self._label_encoder.inverse_transform(transformed_indexes)) + \
                                   ['micro avg', 'macro avg', 'weighted avg']

        return stats_by_class

    def _update_accuracy_by_class_distribution(self):
        matrix = confusion_matrix(self.actual_labels, self._y_preds)
        accuracy_by_class = matrix.diagonal() / matrix.sum(axis=1)
        self._accuracy_by_class = pd.Series(accuracy_by_class).sort_values()

    def load_epoch(self, epoch):  # epoch: range(0, self._total_epochs)
        if epoch not in range(0, self._total_epochs):
            raise KeyError(f"Epoch must be in range [0, {self._total_epochs - 1}]")
        if not hasattr(self, '_weights_by_epoch'):
            raise Exception('You can\'t load an epoch because all epochs except the best one are truncated. '
                            'You may have previously called the "drop_all_epochs_from_dump_file_except_best_epoch" method.')

        self.model.load_state_dict(self._weights_by_epoch['model'][epoch])
        self.optimizer.load_state_dict(self._weights_by_epoch['optimizer'][epoch])
        self._loaded_epoch = epoch
        self._is_metrics_updated = False

    def truncate_dump_file(self, last_untruncated_epoch, truncate_history=False, load_best_epoch_after_truncate=True):
        state = torch.load(self.full_path, map_location='cpu')
        if 'weights_by_epoch' not in state:
            raise Exception('You cannot truncate a dump file that is already truncated. '
                            'You may have called the "drop_all_epochs_from_dump_file_except_best_epoch" method earlier.')

        state['total_epochs'] = last_untruncated_epoch + 1
        state['best_epoch'] = state['history']['val_acc'].index(
            max(state['history']['val_acc'][:last_untruncated_epoch + 1]))

        state['best_model_weights'] = state['weights_by_epoch']['model'][state['best_epoch']]
        state['optimizer_on_best_epoch'] = state['weights_by_epoch']['optimizer'][state['best_epoch']]
        state['weights_by_epoch'] = {key: value[:last_untruncated_epoch + 1]
                                     for key, value in state['weights_by_epoch'].items()}
        self._weights_by_epoch = state['weights_by_epoch']

        if load_best_epoch_after_truncate:
            self.model.load_state_dict(state['best_model_weights'])
            self.optimizer.load_state_dict(state['optimizer_on_best_epoch'])
            self._total_epochs = state['total_epochs']
            self.best_epoch = self._loaded_epoch = state['best_epoch']
        if truncate_history:
            state['history'] = {key: value[:last_untruncated_epoch + 1] for key, value in self._history.items()}

        torch.save(state, self.full_path)

    def drop_all_epochs_from_dump_file_except_best_epoch(self):
        state = torch.load(self.full_path, map_location='cpu')
        state.pop('weights_by_epoch', None)
        torch.save(state, self.full_path)

        del self._weights_by_epoch

    @property
    def protected_attributes(self):
        # Updating the protected attribute view
        self._protected_attributes = {
            'n_classes': self._n_classes, 'num_workers': self._num_workers, 'batch_size': self._batch_size,
            'best_model_wts': self._best_model_wts, 'accuracy_by_class': self._accuracy_by_class,
            'is_metrics_updated': self._is_metrics_updated, 'relative_path': self._relative_path,
            'label_encoder': self._label_encoder, 'figsize': self._figsize,
            'graphics_location': self._graphics_location, 'main_windows_path': self._main_windows_path,
            'main_colab_path': self._main_colab_path, 'device': self._device
        }
        return _ShowAttributeNamesClass(**self._protected_attributes, **{'main_class': self})

    @property
    def y_preds(self):
        if not self._is_metrics_updated:
            self._y_preds = self.predict(self.val_dataset)
        return self._y_preds

    @property
    def loaded_epoch(self):
        return self._loaded_epoch

    @property
    def total_epochs(self):
        return self._total_epochs

    @staticmethod
    def load_label_encoder(full_path):
        with open(full_path, 'rb') as le_dump_file:
            return pickle.load(le_dump_file)

    @staticmethod
    def imshow(inp, title=None, plt_ax=plt,
               mean=np.array([0.485, 0.456, 0.406]),
               std=np.array([0.229, 0.224, 0.225])):
        """Imshow для тензоров"""
        if isinstance(inp, torch.Tensor):
            inp = inp.numpy()
        inp = inp.transpose((1, 2, 0))
        inp = std * inp + mean
        inp = np.clip(inp, 0, 1)
        plt_ax.imshow(inp)
        if title is not None:
            if type(plt_ax) == type(plt):
                plt_ax.title(title, y=1.0, pad=-14)
            else:
                plt_ax.set_title(title, pad=0.5)
        plt_ax.grid(False)

    @classmethod
    def set_main_paths(cls, main_windows_path=None, main_colab_path=None):
        cls._main_windows_path = main_windows_path
        cls._main_colab_path = main_colab_path