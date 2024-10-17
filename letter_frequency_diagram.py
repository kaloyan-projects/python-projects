import matplotlib.pyplot as plt
import regex as re

def count_letter_frequency(file_path):
	# Initialize a dictionary to store the frequency of each letter
	letter_frequency = {}

	# Open the file in read mode
	with open(file_path, 'r') as file:
		# Read the contents of the file
		content = file.read()

		# Skip non-alphabetic characters
		content = re.sub(r'[^\p{L}]', '', content)

		# Iterate over each character in the content
		for char in content:
			# Convert the character to lowercase
			char = char.lower()
			# Increment the count for the current character
			letter_frequency[char] = letter_frequency.get(char, 0) + 1

	return letter_frequency

def main():
	file_path = input("Enter path to file: ")
	letter_frequency = count_letter_frequency(file_path)

	# Sort the letters by their frequency in descending order
	sorted_letters = sorted(letter_frequency.items(), key=lambda x: x[1], reverse=True)

	# Print the letters and their frequency
	print("Frequency of every alphabetic character:")
	for letter, frequency in sorted_letters:
		print(f"{letter}: {frequency}")

	# Create lists for letters and frequencies
	letters = [letter for letter, _ in sorted_letters]
	frequencies = [frequency for _, frequency in sorted_letters]

	# Create a pie chart
	plt.figure(figsize=(8, 8))
	plt.pie(frequencies, labels=letters, autopct='%1.1f%%')
	plt.title("Letter frequency of {}".format(file_path.split("/")[-1]))

	# Save the pie chart to a PNG file
	plt.savefig("letter_frequency_{}.png".format(file_path.split("/")[-1]))
	print("Diagram saved")

	# Display the pie chart
	plt.show()

if __name__ == "__main__":
	main()
