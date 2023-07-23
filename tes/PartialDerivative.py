import numpy as np

vector_a = np.array([-0.12, -0.18])
vector_b = np.array([-12.8, -3.2])
vector_c = np.array([-20.4, -6.8])
hasil = vector_a + vector_b + vector_c

print(f'hasil dari pertambahan vector a,b, dan c = {hasil}\n')

hasil_djdw = hasil/3
print(f'hasil dari partial derivative untuk j terhadap w1 dan w2 = {hasil_djdw}')

# def compute_gradient(x, y, w, b): 
#     """
#     Computes the gradient for linear regression 
#     Args:
#       x (ndarray (m,)): Data, m examples 
#       y (ndarray (m,)): target values
#       w,b (scalar)    : model parameters  
#     Returns
#       dj_dw (scalar): The gradient of the cost w.r.t. the parameters w
#       dj_db (scalar): The gradient of the cost w.r.t. the parameter b     
#      """
    
#     # Number of training examples
#     m = x.shape[0]    
#     dj_dw = 0
#     dj_db = 0
    
#     for i in range(m):  
#         f_wb = np.dot(w, x[i]) + b 
#         dj_dw_i = (f_wb - y[i]) * x[i] 
#         dj_db_i = f_wb - y[i] 
#         dj_db += dj_db_i
#         dj_dw += dj_dw_i 
#     dj_dw = dj_dw / m 
#     dj_db = dj_db / m 
        
#     return dj_dw, dj_db

# data_points = np.array([
#     [2, 3, 5],
#     [4, 1, 7],
#     [6, 2, 9]
# ])

# # Extract the features (x1, x2) and target variable (y)
# x = data_points[:, :2]
# y = data_points[:, 2]

# w1_w2= np.array([0.5, 0.8])

# b = 1

# dj_dw, dj_db = compute_gradient(x,y,w1_w2,b)

# print(f'hasil dj_dw {dj_dw}')
# print(f'hasil dj_db {dj_db}')