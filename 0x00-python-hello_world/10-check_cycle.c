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

	if (list == NULL || list->next == NULL || (list->next)->next == NULL)
		return (0);

	temp = (list->next)->next;

	while (list != NULL)
	{
		if (temp == list)
		{
			return (1);
		}
		if (temp != NULL)
		{
			if (temp->next != NULL && (temp->next)->next != NULL)
				temp = (temp->next)->next;
			else
				temp = NULL;
		}
		list = list->next;
	}
	return (0);
}
