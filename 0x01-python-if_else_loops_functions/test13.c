#include "lists.h"

/**
 * main - test function
 *
 * Return: 0
 */
int main(void)
{
	listint_t *head = NULL;
	size_t numNode;

	add_nodeint_end(&head, 0);
	add_nodeint_end(&head, 1);
	add_nodeint_end(&head, 2);
	add_nodeint_end(&head, 3);
	add_nodeint_end(&head, 4);
	add_nodeint_end(&head, 98);
	add_nodeint_end(&head, 402);
	add_nodeint_end(&head, 1024);
	numNode = print_listint(head);
	printf("Number of Nodes: %lu\n", numNode);
	insert_node(&head, 2048);
	insert_node(&head, 495);
	insert_node(&head, 100);
	insert_node(&head, 5);
	insert_node(&head, -2);
	print_listint(head);
	free_listint(head);
	return (0);
}
