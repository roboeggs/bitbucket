#include <iostream>
#include <cstdlib>

struct node {
    int data;
    node* left;
    node* right;
};

void insert(node** tree, int val) {
    node* temp = NULL;
    if (!(*tree)) {
        temp = (node*)malloc(sizeof(node));
        temp->left = temp->right = NULL;
        temp->data = val;
        *tree = temp;
        return;
    }

    if (val < (*tree)->data) {
        insert(&(*tree)->left, val);
    }
    else if (val > (*tree)->data) {
        insert(&(*tree)->right, val);
    }
}

node* findMin(node* tree) {
    while (tree->left != NULL) {
        tree = tree->left;
    }
    return tree;
}

void deleteNode(node** tree, int val) {
    if (!(*tree)) {
        return;
    }

    if (val < (*tree)->data) {
        deleteNode(&(*tree)->left, val);
    }
    else if (val > (*tree)->data) {
        deleteNode(&(*tree)->right, val);
    }
    else {
        if ((*tree)->left && (*tree)->right) {
            node* temp = findMin((*tree)->right);
            (*tree)->data = temp->data;
            deleteNode(&(*tree)->right, temp->data);
        }
        else {
            node* temp = *tree;
            if ((*tree)->left == NULL) {
                *tree = (*tree)->right;
            }
            else if ((*tree)->right == NULL) {
                *tree = (*tree)->left;
            }
            free(temp);
        }
    }
}

void printTree(node* tree) {
    if (tree == NULL) {
        return;
    }

    printTree(tree->left);
    std::cout << tree->data << " ";
    printTree(tree->right);
}


int main() {
    node* root;
    root = NULL;
    // Вставка значений
    insert(&root, 9);
    insert(&root, 4);
    insert(&root, 15);
    insert(&root, 6);
    insert(&root, 12);
    insert(&root, 17);
    insert(&root, 2);

    // Печать дерева
    printTree(root);
    std::cout << std::endl;

    // Удаление значения
    deleteNode(&root, 9);

    // Печать дерева
    printTree(root);
    std::cout << std::endl;

    return 0;
}
