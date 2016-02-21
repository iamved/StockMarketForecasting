from __future__ import print_function
print(__doc__)
import numpy as np 
import matplotlib.pyplot as plt 
from mpl_toolkits.mplot3d import Axes3D
from sklearn.model_selection import train_test_split
from sklearn.ensemble import GradientBoostingRegressor
from sklearn.ensemble.partial_dependence import plot_partial_dependence
from sklearn.ensemble.partial_dependence import partial_dependence
from sklearn.ensemble.california_housing import fetch_california_housing

def main():
	cal_housing = fetch_california_housing()
	X_train, X_test, y_train , y_test = train_test_split(cal_housing.data,
		                                                 cal_housing.target,
		                                                 test_size =0.2,
		                                                 ramdom_state =1)
	name=cal_housing.feature_names

    print("Training GBRT ...", flush =True, end='')
    
    clf = GradientBoostingRegressor(n_estimators =100, max_depth=4,
    	                            learning_rate =0.1,loss='huber',
    	                            random_state =1)
    clf.fit(X_train,y_train)
    print("done.")
    print('Convenience plot with partiaql_dependence_plots')
    features =[0,5,1,2,(5,1)]
    fig, axs =plot_partial_dependence(clf,X_train,features,
    	                             feature_names=names,
    	                             n_jobs=3,grid_resolution=50)
    XX, YY=np.meshgrid(axes[0],axes[1])
    Z = pdp[0].reshape(list(map(np.size,axes))).T 
    ax =Axes3D(fig)
    surf =ax.plot_surface(XX, YY, Z,rstride=1,cstride=1.cmap=plt.cm.BuPu)
    ax.set_xlable(names[target_feature[0]])
    ax.set_ylabel(names[target_feature[1]])
    ax.set_zlabel('partial_dependence')
    ax.view_init(elev =22,azim=122)
    plt.colorbar(surf)
    plt.suptitle('Partial dependence of house value on median age and '
    	         'average occupancy')
    plt.subplots_adjust(top=0.9)
    plt.show()
    if __name__ =='__main__':
    	main()