# Define a basic class called 'Student'.
class Student:
    # This method makes the student say a friendly greeting.
    def hello(self):
        print("Hey there! I'm so excited to learn stuff.")
    
    # This method makes the student show they want to answer a question.
    def raise_hand(self):
        print("Pick me!")

# Define a special version of the 'Student' class called 'ChattyStudent'.
# 'ChattyStudent' inherits from the 'Student' class.
class ChattyStudent(Student):
    # This method is like the 'hello' method in 'Student',
    # but it adds a lot more chit-chat.
    def hello(self):
        # Call the 'hello' method in the 'Student' class first.
        super().hello()
        # Add some extra chatty information.
        print("How are you doing today? I'm okay, but I'm kind of tired. Did you watch The Walking Dead last night? You didn't?! Oh man, it was so crazy! What, you don't want any spoilers? Okay well let me just tell you who died...")
    # This method is like the 'raise_hand' method in 'Student',
    # but it raises the hand multiple times.
    def raise_hand(self):
        # Repeat raising the hand 10 times.
        for _ in range(10):
            # Call the 'raise_hand' method in the 'Student' class.
            super().raise_hand()

    