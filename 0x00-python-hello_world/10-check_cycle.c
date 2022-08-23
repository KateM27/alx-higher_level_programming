#include "lists.h"

/**
 * check_cycle - checks to see if a list has a cycle in it
 * @list: the list to check
 * Return: 0 if there's no cycle, 1 if there is a cycle
 */

int check_cycle(listint_t *list)
{
	listint_t *d2 = list;
	listint_t *prev = list;

	if (list == NULL)
		return (0);

	while (d2 && d2->next)
	{
		prev = prev->next;
		d2 = d2->next->next;

		if (prev == d2)
			return (1);
	}
	return (0);
}
