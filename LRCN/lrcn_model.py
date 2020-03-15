import torch.nn as nn
from torchvision import models

<<<<<<< HEAD

=======
>>>>>>> c139c9917a10d56fee85a67d8fbe6c84dfd80b13
class ConvLstm(nn.Module):
    def __init__(self, latent_dim, model, hidden_size, lstm_layers, bidirectional, n_class):
        super(ConvLstm, self).__init__()
        self.conv_model = Pretrained_conv(latent_dim, model)
        self.Lstm = Lstm(latent_dim, hidden_size, lstm_layers, bidirectional)
        self.output_layer = nn.Sequential(
<<<<<<< HEAD
            nn.Linear(2 * hidden_size if bidirectional ==
                      True else hidden_size, n_class),
=======
            nn.Linear(2 * hidden_size if bidirectional==True else hidden_size, n_class),
>>>>>>> c139c9917a10d56fee85a67d8fbe6c84dfd80b13
            nn.Softmax(dim=-1)
        )

    def forward(self, x):
        batch_size, timesteps, channel_x, h_x, w_x = x.shape
        conv_input = x.view(batch_size * timesteps, channel_x, h_x, w_x)
        conv_output = self.conv_model(conv_input)
        lstm_input = conv_output.view(batch_size, timesteps, -1)
        lstm_output = self.Lstm(lstm_input)
        lstm_output = lstm_output[:, -1, :]
        output = self.output_layer(lstm_output)
        return output

<<<<<<< HEAD

=======
>>>>>>> c139c9917a10d56fee85a67d8fbe6c84dfd80b13
class Pretrained_conv(nn.Module):
    def __init__(self, latent_dim, model):
        if model == 'resnet152':
            super(Pretrained_conv, self).__init__()
            self.conv_model = models.resnet152(pretrained=True)
            # ====== freezing all of the layers ======
            for param in self.conv_model.parameters():
                param.requires_grad = False
            # ====== changing the last FC layer to an output with the size we need. this layer is un freezed ======
<<<<<<< HEAD
            self.conv_model.fc = nn.Linear(
                self.conv_model.fc.in_features, latent_dim)
=======
            self.conv_model.fc = nn.Linear(self.conv_model.fc.in_features, latent_dim)
>>>>>>> c139c9917a10d56fee85a67d8fbe6c84dfd80b13
        elif model == 'densenet201':
            super(Pretrained_conv, self).__init__()
            self.conv_model = models.densenet201(pretrained=True)
            # ====== freezing all of the layers ======
            for param in self.conv_model.parameters():
                param.requires_grad = False
            # ====== changing the last FC layer to an output with the size we need. this layer is un freezed ======
<<<<<<< HEAD
            self.conv_model.classifier = nn.Linear(
                self.conv_model.classifier.in_features, latent_dim)
=======
            self.conv_model.classifier = nn.Linear(self.conv_model.classifier.in_features, latent_dim)
>>>>>>> c139c9917a10d56fee85a67d8fbe6c84dfd80b13
        elif model == 'densenet161':
            super(Pretrained_conv, self).__init__()
            self.conv_model = models.densenet161(pretrained=True)
            # ====== freezing all of the layers ======
            for param in self.conv_model.parameters():
                param.requires_grad = False
            # ====== changing the last FC layer to an output with the size we need. this layer is un freezed ======
<<<<<<< HEAD
            self.conv_model.classifier = nn.Linear(
                self.conv_model.classifier.in_features, latent_dim)
=======
            self.conv_model.classifier = nn.Linear(self.conv_model.classifier.in_features, latent_dim)
>>>>>>> c139c9917a10d56fee85a67d8fbe6c84dfd80b13

    def forward(self, x):
        return self.conv_model(x)

<<<<<<< HEAD

class Lstm(nn.Module):
    def __init__(self, latent_dim, hidden_size, lstm_layers, bidirectional):
        super(Lstm, self).__init__()
        self.Lstm = nn.LSTM(latent_dim, hidden_size=hidden_size,
                            num_layers=lstm_layers, batch_first=True, bidirectional=bidirectional)
=======
class Lstm(nn.Module):
    def __init__(self, latent_dim, hidden_size, lstm_layers, bidirectional):
        super(Lstm, self).__init__()
        self.Lstm = nn.LSTM(latent_dim, hidden_size=hidden_size, num_layers=lstm_layers, batch_first=True, bidirectional=bidirectional)
>>>>>>> c139c9917a10d56fee85a67d8fbe6c84dfd80b13
        self.hidden_state = None

    def reset_hidden_state(self):
        self.hidden_state = None

<<<<<<< HEAD
    def forward(self, x):
        output, self.hidden_state = self.Lstm(x, self.hidden_state)
        return output
=======
    def forward(self,x):
        output, self.hidden_state = self.Lstm(x, self.hidden_state)
        return output

>>>>>>> c139c9917a10d56fee85a67d8fbe6c84dfd80b13
