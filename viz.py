import pandas, sys
import matplotlib.pyplot as plt

from sklearn import linear_model
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error, r2_score

playlist_category = sys.argv[1:][0]

all_tracks = pandas.read_csv(filepath_or_buffer="./data/all_tracks_"+playlist_category+".csv")
keep_features = all_tracks[['id', 'acousticness', 'danceability', 'duration_ms', 'energy', 'instrumentalness', 'key', 'liveness', 'loudness', 'mode', 'speechiness', 'tempo', 'time_signature', 'valence', 'explicit', 'popularity', 'track_number']]

#all_tracks.plot.scatter(x='track_number', y='popularity')
#plt.show()

# plt.matshow(keep_features.corr())
# plt.xticks(range(keep_features.shape[1]), keep_features.columns, fontsize=14, rotation=45)
# plt.yticks(range(keep_features.shape[1]), keep_features.columns, fontsize=14)
# plt.show()

X = keep_features[['acousticness', 'danceability', 'duration_ms', 'energy', 'instrumentalness', 'key', 'liveness', 'loudness', 'mode', 'speechiness', 'tempo', 'time_signature', 'valence', 'explicit', 'track_number']]
y = keep_features['popularity']

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=.15, random_state=10)

lin_reg = linear_model.LinearRegression()
lin_reg.fit(X_train,y_train)

y_pred = lin_reg.predict(X_test)
print(len(X_test) == len(y_test))

# The coefficients
print('Coefficients: \n', lin_reg.coef_)
# The mean squared error
print('Mean squared error: %.2f'
      % mean_squared_error(y_test, y_pred))
# The coefficient of determination: 1 is perfect prediction
print('Coefficient of determination: %.2f'
      % r2_score(y_test, y_pred))

plt.scatter(X_test, y_test,  color='black')
#plt.plot(X_test, y_pred, color='blue', linewidth=3)

plt.xticks(())
plt.yticks(())

plt.show()