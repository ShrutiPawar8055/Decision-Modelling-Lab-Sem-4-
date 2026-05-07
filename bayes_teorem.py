# Training data (Offer, Free, Class)
train_data = [
    ("Yes","Yes","Spam"),
    ("Yes","No","Spam"),
    ("No","Yes","Spam"),
    ("Yes","No","Ham"),
    ("No","No","Ham")
]

# Test data
test_data = [
    ("Yes","Yes","Spam"),
    ("No","No","Ham"),
    ("Yes","No","Spam"),
    ("No","Yes","Spam")
]

# Separate classes
spam = [d for d in train_data if d[2] == "Spam"]
ham = [d for d in train_data if d[2] == "Ham"]

# Prior probabilities
P_spam = len(spam) / len(train_data)
P_ham = len(ham) / len(train_data)

# Likelihood with Laplace smoothing
def likelihood(dataset, index, value):
    count = sum(1 for d in dataset if d[index] == value)
    return (count + 1) / (len(dataset) + 2)

# Prediction function
def predict(sample):
    P_spam_x = P_spam * likelihood(spam,0,sample[0]) * likelihood(spam,1,sample[1])
    P_ham_x  = P_ham  * likelihood(ham,0,sample[0])  * likelihood(ham,1,sample[1])

    if P_spam_x > P_ham_x:
        return "Spam"
    else:
        return "Ham"

# Testing
correct = 0

print("TEST RESULTS\n")

for row in test_data:
    sample = row[:2]
    actual = row[2]
    predicted = predict(sample)

    print("Sample:", sample)
    print("Actual:", actual, "| Predicted:", predicted)
    print()

    if predicted == actual:
        correct += 1

accuracy = correct / len(test_data)
print("Final Accuracy:", accuracy)