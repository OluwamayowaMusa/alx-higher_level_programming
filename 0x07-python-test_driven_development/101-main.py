#!/usr/bin/python3
lazy_matrix_mul = __import__("101-lazy_matrix_mul").lazy_matrix_mul

m_b = [[]]
m_a = [[5, 6], [7, 8]]
try:
    print(lazy_matrix_mul(m_a, m_b))
except Exception as e:
    print(e)

print("--")
m_a = [[]]
m_b = [[5, 6], [7, 8]]
try:
    print(lazy_matrix_mul(m_a, m_b))
except Exception as e:
    print(e)
    
print("--")
m_a = [[5, 6], [7, 8]]
m_b = [[5, 6, 1], [7, 8]]
try:
    print(lazy_matrix_mul(m_a, m_b))
except Exception as e:
    print(e)

print("--")
m_a = [[1, 2, 3], [3, 4, 5]]
m_b = [[1, 2], [3, 4]]
try:
    print(lazy_matrix_mul(m_a, m_b))
except Exception as e:
    print(e)
