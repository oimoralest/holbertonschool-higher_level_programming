#include "lists.h"
/**
 * check_cycle - check if a singly linked list has a cycle in it
 * @list: head of the list
 * Return: 0 if there is no cycle, 1 if there is a cycle
 */
int check_cycle(listint_t *list)
{
	listint_t *aux, *aux2;

	if (!list || !list->next)
	{
		return (0);
	}
	else
	{
		aux = list, aux2 = list->next;
		while (aux != aux2 && aux2->next && aux2->next->next
			&& aux->next)
		aux = aux->next, aux2 = aux2->next->next;
		if (aux == aux2)
			return (1);
		else
			return (0);
	}
}
