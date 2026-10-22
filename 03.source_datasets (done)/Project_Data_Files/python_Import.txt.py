
# Install the ucimlrepo package
#   pip install ucimlrepo
#   pip install ucimlrepo


# Import the dataset into your code 

from ucimlrepo import fetch_ucirepo 
  
# fetch dataset 
multivariate_gait_data = fetch_ucirepo(id=760) 
  
# data (as pandas dataframes) 
X = multivariate_gait_data.data.features 
y = multivariate_gait_data.data.targets 
  
# metadata 
print(multivariate_gait_data.metadata) 
  
# variable information 
print(multivariate_gait_data.variables) 



