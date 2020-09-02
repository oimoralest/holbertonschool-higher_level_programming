#include "lists.h"
/**
 * insert_node - insert a number in a sorted singly linked list
 * @head: head of the linked list
 * @number: number to insert
 * Return: the address of the new node, or NULL if it failed
 */
listint_t *insert_node(listint_t **head, int number)
{
	listint_t *aux, *new_node;

	if (!head)
		return (NULL);
	new_node = malloc(sizeof(listint_t));
	if (!new_node)
		return (NULL);
	new_node->n = number;
	if (!*head || (*head)->n >= number)
	{
		new_node->next = *head;
		*head = new_node;
	}
	else
	{
		aux = *head;
		while (aux)
		{
			if (!aux->next || aux->next->n >= number)
				break;
			aux = aux->next;
		}
		new_node->next = aux->next;
		aux->next = new_node;
	}

	return (new_node);
}
