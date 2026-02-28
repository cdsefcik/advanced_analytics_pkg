from advanced_analytics_pkg import advancedanalytics

# Initialize the class
aa = advancedanalytics()

# Data to process
numbers = [10.0, 20.0, 30.0, 40.0]

# Calculate
avg = aa.compute_mean(numbers)
print(f"The mean value is: {avg}") # Output: 25.0