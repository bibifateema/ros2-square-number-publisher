ROS 2 Square Number Publisher
A simple ROS 2 Python publisher that publishes the squares of numbers from 1 to 10 repeatedly.

Features

Starts counting from 1

Calculates the square of each number

Publishes squares from 1 to 10

Resets the counter to 1 after reaching 10

Uses an if-else condition for counter reset

Timer-based publishing (1 second interval)

Topic

square_numbers

Message Type

std_msgs/msg/Int32

Expected Output

1, 4, 9, 16, 25, 36, 49, 64, 81, 100

Then repeats from 1.
