from keras.models import load_model

class Classifier:
    def __init__(self):
        self.feature_extractor = load_model('model/patch_feature_extractor_model_preprocesse.h5')
        self.feature_classifier = load_model('model/patch_classifier_model_preprocesse.h5')
        self.timesteps = 6
        self.number_of_features = 512

    def _get_features(self, patches):
        # Feature extraction
        features = self.feature_extractor.predict(patches)
        return features

    def get_predictions(self, patches, threshold):
        features = self._get_features(patches)
        # Feature classification
        features_reshaped = features.reshape(-1, self.timesteps, self.number_of_features)
        predicted_label = self.feature_classifier.predict(features_reshaped)
        predicted_label = (predicted_label > threshold).astype(int) # Binary classification Benign =0, Malignant =1
        return predicted_label