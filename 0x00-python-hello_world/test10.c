#include "lists.h"
#include <time.h>

/**
 * main - test function
 *
 * Return: 0
 */
int main(void)
{
	listint_t *head, *current, *temp, *reset;
	clock_t start, end, diff;
	size_t i;

	head = NULL;
	add_nodeint(&head, 0);
	add_nodeint(&head, 1);
	add_nodeint(&head, 2);
	add_nodeint(&head, 3);
	add_nodeint(&head, 4);
	add_nodeint(&head, 98);
	add_nodeint(&head, 402);
	add_nodeint(&head, 972);
	add_nodeint(&head, 1024);
	add_nodeint(&head, 2048);
	print_listint(head);
	start = clock();
	if (check_cycle(head) == 0)
		printf("Linked list has no cycle\n");
	else if (check_cycle(head) == 1)
		printf("Linked list has a cycle\n");
	end = clock();
	diff = (double)(end - start) / 10;
	printf("Time taken: %ld\n", diff);
	current = head;
	for (i = 0; i < 6; i++)
	{
		if (i == 4)
			temp = current;
		current = current->next;
	}
	reset = current->next;
	current->next = temp;
	start = clock();
	if (check_cycle(head) == 0)
		printf("Linked list has no cycle\n");
	else if (check_cycle(head) == 1)
		printf("Linked list has a cycle\n");
	end = clock();
	diff = (double)(end - start) / 10;
	printf("Time taken: %ld\n", diff);
	current = head;
	for (i = 0; i < 4; i++)
		current = current->next;
	current->next = reset;

	free_listint(head);
	return (0);
}
