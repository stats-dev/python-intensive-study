# Build histogram with 5 bins
plt.hist(life_exp, bins=5)

# Show and clean up plot
plt.show()
plt.clf()

# Build histogram with 20 bins
plt.hist(life_exp, bins=20)

# Show and clean up again
plt.show()
plt.clf()

# bin을 늘려두면, 좀 더  촘촘하다. 그러나 무조건 늘린다고 좋지 않다. 패턴이 잘 보인다.