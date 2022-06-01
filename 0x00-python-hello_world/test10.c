#include "lists.h"

/**
 * main - test function
 *
 * Return: 0
 */
int main(void)
{
	listint_t *head, *current, *temp;
	size_t numNode, i;

	head = NULL;
	add_nodeint(&head, 0);
	add_nodeint(&head, 1);
	add_nodeint(&head, 2);
	add_nodeint(&head, 3);
	add_nodeint(&head, 4);
	add_nodeint(&head, 98);
	add_nodeint(&head, 402);
	add_nodeint(&head, 1024);
	numNode = print_listint(head);
	printf("Number of nodes: %lu\n", numNode);
	if (check_cycle(head) == 0)
		printf("Linked list has no cycle\n");
	else if (check_cycle(head) == 1)
		printf("Linked list has a cycle\n");

	current = head;
	for (i = 0; i < 4; i++)
		current = current->next;
	temp = current->next;
	current->next = head;
	if (check_cycle(head) == 0)
		printf("Linked list has no cycle\n");
	else if (check_cycle(head) == 1)
		printf("Linked list has a cycle\n");
	current = head;
	for (i = 0; i < 4; i++)
		current = current->next;
	current->next = temp;

	free_listint(head);
	return (0);
}