#  build a class MeanRegressor that can be initialized
class MeanRegressor:
    

    def fit(self, X, y):
        y_mean = y.mean() 
        self.y_mean = y_mean

    def predict(self, X):
        # X is a two-dimensional matrix
        # returns the mean of the training data for each row of X in a list
        X_means = []
        for _ in range(len(X)):
            X_means.append(self.y_mean)
        self.X_means = X_means
        return X_means
        # self.score(X_means)

    def score(self, X, y):
        # self.predict(X)
        residual_sum_of_squares = sum((y - self.y_mean)**2)
        total_sum_of_squares = sum((y - y.mean())**2)
        # print(residual_sum_of_squares, total_sum_of_squares)
        return 1 - residual_sum_of_squares/total_sum_of_squares

        # rss = sum(lambda y, self.X_means: actual - self.X_means for actual in y)