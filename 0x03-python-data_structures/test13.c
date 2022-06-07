#include "lists.h"
#include <time.h>

/**
 * main - Test function
 *
 * Return: 0
 */
int main(void)
{
	listint_t *head;
	clock_t start, end, diff;

	head = NULL;
	add_nodeint_end(&head, 1);
	add_nodeint_end(&head, 2);
	add_nodeint_end(&head, 3);
	add_nodeint_end(&head, 4);
	add_nodeint_end(&head, 3);
	add_nodeint_end(&head, 2);
	add_nodeint_end(&head, 1);
	print_listint(head);

	start = clock();
	if (is_palindrome(&head) == 1)
		printf("Linked list is a palindrome\n");
	else
		printf("Linked list is not a palindrome\n");
	end = clock();
	diff = (double)(end - start) / 10;
	printf("Time taken: %f\n", (double)diff);
	free_listint(head);
	return (0);
}
