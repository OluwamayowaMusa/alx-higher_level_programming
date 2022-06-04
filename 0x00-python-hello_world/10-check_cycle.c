#include "lists.h"


/**
 * check_cycle - check if there is a loop in linked list(a cycle)
 * @list: Pointer to linked list
 *
 * Return: 0 - If there is no cycle
 *         1 - if there is cycle
 */
int check_cycle(listint_t *list)
{
	listint_t *temp = NULL;
	
	if (list == NULL)
		return (0);
	temp = list->next;

	while (temp != NULL)
	{
		if (temp == list)
		{
			return (1);
		}
		temp = temp->next;
	}
	return (0);
}
