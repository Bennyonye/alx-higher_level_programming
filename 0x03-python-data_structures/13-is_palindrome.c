#include "lists.h"
#include <stdlib.h>
#include <stdio.h>

/**
 * is_palindrome - Identifies if a single linked list is palindrome
 * @head: Pointer to the head of listint_t
 * Return: 1 if it is palindrome, else 0
 */
int is_palindrome(listint_t **head)
{
    if (head == NULL || *head2 == NULL)
        return (1);
    return (aux_palind(head, *head));
}

/**
 * aux_palind - function to know if is palindrome
 * @head: head of list
 * @end: end of list
 */
 int aux_palind(listint_t **head, listint_t *end)
 {
    if (end == NULL)
        return (1);
    if (aux_palind(head, end->next) && (*head)-> == end->n)
    {
                *head = (*head)->next;
                return (1);
    }
    return (0);
 }
