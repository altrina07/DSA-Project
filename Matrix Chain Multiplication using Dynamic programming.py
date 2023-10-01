def matrix_chain_multiplication(matrices):
    n = len(matrices)
    
    # Initialize a table to store minimum scalar multiplications
    dp = [[0] * n for _ in range(n)]
    
    # Initialize a table to store optimal parenthesizations
    parenth = [[0] * n for _ in range(n)]
    
    # Fill the table using bottom-up dynamic programming
    for chain_length in range(2, n):
        for i in range(1, n - chain_length + 1):
            j = i + chain_length - 1
            dp[i][j] = float('inf')  # Initialize with infinity
            
            for k in range(i, j):
                cost = dp[i][k] + dp[k + 1][j] + matrices[i - 1][0] * matrices[k][1] * matrices[j][1]
                
                if cost < dp[i][j]:
                    dp[i][j] = cost
                    parenth[i][j] = k
    
    # Reconstruct the optimal parenthesization
    def print_parenthesization(i, j):
        if i == j:
            return "A{}".format(i)
        else:
            k = parenth[i][j]
            left_chain = print_parenthesization(i, k)
            right_chain = print_parenthesization(k + 1, j)
            return "({} x {})".format(left_chain, right_chain)
    
    optimal_parenthesization = print_parenthesization(1, n - 1)
    
    return optimal_parenthesization, dp[1][n - 1]

# Example input
matrices = [(2, 3), (3, 4), (4, 2)]

# Apply the matrix chain multiplication algorithm
optimal_parenthesization, min_scalar_multiplications = matrix_chain_multiplication(matrices)

print("Optimal Parenthesization:", optimal_parenthesization)
print("Minimum Scalar Multiplications:", min_scalar_multiplications)
