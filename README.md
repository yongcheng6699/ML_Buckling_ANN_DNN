# Data-driven-Mechanics

### Contains code and analysis related to projects centering on data-driven analysis.
### Buckling of perforations C-section predictions

### What is happening here?
### [1] A traditional ANN model with 1-hidden layer and the deep DNN model with 2, 3, and 4-hidden layers.
### [2] Import and preprocessing data with the Ansys simulated results.
### [3] Trigonometric transformations, which converting the original angle plies into sine and cosine values range between -1 and 1 to helps normalize data.
### [4] Create a neural network model with specific hidden layer and the model uses the Sequential API from Keras, starting with an input layer, followed by a dense (fully connected) hidden layer with ReLU activation, and then an output layer with linear activation (for regression tasks).
### [5] Model Training and Evaluation:  Construct 5-Fold Cross-Validation and run over a range of different number of neurons (from 20 to 80 with step of 15) to tune the model's hyperparameters. For each number of neurons: A KerasRegressor wrapper is instantiated with the defined neural network model and training settings (epochs, batch size). 
### [6] After K Fold cross validation, the dataset is split into training and testing sets. Then, a validation set allows monitoring the model's performance on unseen data during training, which helps in early stopping and preventing overfitting.
### [7] Find the best neural network model with specific neurons in hidden layer to do the Model Evaluation (Performance metrics).
### [8] Plot loss vs the number of epochs & MAE vs the number of epochs
### [9] Plot Correlation between the actual output and the predicted output with the training dataset
### [10] Plot Correlation between the actual output and the predicted output with the testing dataset
### [11] Lastly, SHAP (SHapley Additive exPlanations) values are computed to explain variable importance in the model using shap library. SHAP summary plots (shap.summary_plot) are created to show the impact of different features on the model predictions.
