#include "lists.h"

/**
 * free_list - Free linked list
 * @head: Pointer to linked list
 *
 */
void free_list(listint_t *head)
{
	listint_t *current = NULL;

	while (head != NULL)
	{
		current = head->next;
		free(head);
		head = current;
	}
}

/**
 * check_num - check for numner in linked list
 * @num: Number
 * @head: pointer to linked list
 *
 * Return: 1 - if present
 *         0 - otherwise
 */
int check_num(int num, listint_t *head)
{
	if (head == NULL)
		return (0);
	while (head != NULL)
	{
		if (head->n == num)
			return (1);
		head = head->next;
	}
	return (0);
}


/**
 * add_nodeint - Add node to linked list
 * @head: Pointer to pointer to linked list
 * @n: data
 *
 * Return: Address of new node
 */
listint_t *add_nodeint(listint_t **head,  const int n)
{
	listint_t *newNode = NULL;

	newNode = malloc(sizeof(listint_t));
	if (newNode == NULL)
		return (NULL);
	newNode->n = n;
	newNode->next = *head;
	*head = newNode;
	return (newNode);
}


/**
 * is_palindrome - Checks if a linked list is a panlindrome
 * @head: Pointer to pointer to linked List
 *
 * Return: 0 - if not a palindrome
 *         1 - if it is a palindrome
 */
int is_palindrome(listint_t **head)
{
	listint_t *storeNode = NULL, *temp, *temp1;
	int ctrl = 1;

	if (head == NULL)
		return (0);
	if (*head == NULL)
		return (1);
	temp = *head;
	while (temp != NULL)
	{
		if (check_num(temp->n, storeNode) == 0)
			add_nodeint(&storeNode, temp->n);
		else if (check_num(temp->n, storeNode) == 1)
			break;
		temp = temp->next;
	}
	temp1 = storeNode;
	while (storeNode != NULL && temp != NULL)
	{
		if (storeNode->n != temp->n)
		{
			ctrl = 0;
			break;
		}
		storeNode = storeNode->next;
		temp = temp->next;
	}
	if (temp != NULL || storeNode != NULL)
		ctrl = 0;
	free_list(temp1);
	return (ctrl);
}
