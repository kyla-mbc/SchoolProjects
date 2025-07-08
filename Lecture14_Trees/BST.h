#ifndef BST_H
#define BST_H

#include "TreeNode.h"


template <typename T>
class BST{
    public:
        BST();
        virtual ~BST();
        // contains: is this data d in the tree?
        bool contains(T d); // recursive version
        bool iterContains(T d); // iterative version
        // print methods 
        void printInOrder(); // least to greatest order 
        void printPostOrder(); 

        // insert 
        void insert(T d);

        // remove 
        void remove(T key);

        // size
        int size();

        // extrema
        T max();
        T min(); 
        T naiveMedian(); // return the root, will be median if tree happens to be perfectly balanced & full


        //participation from lecture 17, height of tree
        int maxDepth();

    private:
        TreeNode<T>* m_root; 
        int m_size;
        // helper methods for recursive methods 
        void destroyTree(TreeNode<T>* node);

        bool containsHelper(TreeNode<T>* n, T d);
        void printIOHelper(TreeNode<T>* n);
        void printPOHelper(TreeNode<T>* n);

        void insertHelper(TreeNode<T>*& n, T& d);

        T getMaxHelper(TreeNode<T>* n);
        T getMinHelper(TreeNode<T>* n);

        void findTarget (T key, TreeNode<T>*& target, TreeNode<T>*& parent);
        TreeNode<T>* getSuccessor (TreeNode<T>* rightChild);
};

// ***************************************************************** // 
// ****************** LECTURE  15 ********************************** // 
// ***************************************************************** // 

// CONSTRUCTOR
template <typename T>
BST<T>::BST(){
    m_root = NULL;
    m_size = 0;
}

// DESTRUCTOR
template <typename T>
BST<T>::~BST(){
    // TO DO
    destroyTree(m_root); // Helper function to delete all nodes

}
// ACTIVITY:
template <typename T>
void BST<T>::destroyTree(TreeNode<T>* node) {
    if (node != NULL) {
        destroyTree(node->m_left);  // Recursively delete the left subtree
        destroyTree(node->m_right); // Recursively delete the right subtree
        delete node;                // Delete the current node
    }
}

// SIZE 
template <typename T>
int BST<T>::size(){
    return m_size;
}

// ITERATIVE CONTAINS (returns true or false whether data d is found in tree)
// do any nodes in the tree contain data == d?
template <typename T>
bool BST<T>::iterContains(T d){
    if(m_root == NULL){ // tree is empty, d is not here 
        return false;
    }
    if(m_root -> m_data == d){ // root has data == d 
        return true;
    }

    // look for d elsewhere
    bool found = false; 
    TreeNode<T>* current = m_root;

    while (!found){
        //check: should we go left or right?
        if (d > current -> m_data){ // right of current 
            current = current -> m_right;
        } else { // go left of current
            current = current -> m_left; 
        }
        // is the current node null? 
        if (current == NULL){
            // the data d is not in our tree 
            found = false; 
            break;
        }
        // does the current node have our data d?
        if (current -> m_data == d){
            found = true; 
            break;
        }
    }
    return found;
}

// RECURSIVE COINTAINS 
template <typename T>
bool BST<T>::contains(T d){ // public interface 
    return containsHelper(m_root, d);
}

template <typename T>
bool BST<T>::containsHelper(TreeNode<T>* n, T d){ // the actual logic 
    if (n == NULL){ // finished looking thru tree and d was not found
        return false; 
    } 
    if (n -> m_data == d){ // current node n has the data d 
        return true;
    }
    if (d > n -> m_data){ // go right
        return containsHelper(n -> m_right, d);
    } else { // go left
        return containsHelper(n -> m_left, d);
    }
}

// PRINT ELEMENTS IN ORDER LEAST TO GREATEST 
template <typename T>
void BST<T>::printInOrder(){
    printIOHelper(m_root);
}

template <typename T>
void BST<T>::printIOHelper(TreeNode<T>* n){
    if (n != NULL){
        printIOHelper(n -> m_left);
        std::cout << n -> m_data << std::endl;
        printIOHelper(n -> m_right);
    }
}


// PRINT ELEMENTS IN POST ORDER (deepest subtree left, deepest subtree right to root)
template <typename T>
void BST<T>::printPostOrder(){
    printPOHelper(m_root);
}

template <typename T>
void BST<T>::printPOHelper(TreeNode<T>* subTreeRoot){
    if(subTreeRoot != NULL){
        printPOHelper(subTreeRoot->m_left);
        printPOHelper(subTreeRoot->m_right);
        cout << subTreeRoot->m_data << endl;
    }
}


// INSERT
template <typename T>
void BST<T>::insert(T d){
    insertHelper(m_root, d);
    ++m_size;
}

template <typename T>
void BST<T>::insertHelper(TreeNode<T>*& n, T& d){ // accessing the node & data directly 
    if (n == NULL){ 
        n = new TreeNode<T>(d);
    } else if (d > n -> m_data){
        insertHelper(n->m_right, d);
    } else {
        insertHelper(n->m_left, d);
    }
}

// GET MAX VALUE IN TREE: where would it be?
template <typename T>
T BST<T>::max(){
    return getMaxHelper(m_root);
}

template <typename T>
T BST<T>::getMaxHelper(TreeNode<T>* n){
    if (n -> m_right == NULL){ // can't go further right, this is the max
        return n -> m_data;
    } else {
        return getMaxHelper(n -> m_right);
    }
}

// GET MIN VALUE IN TREE: where would it be?
template <typename T>
T BST<T>::min(){
    return getMinHelper(m_root);
}
template <typename T>
T BST<T>::getMinHelper(TreeNode<T>* n){
    if (n -> m_left == NULL){ // can't go further right, this is the max
        return n -> m_data;
    } else {
        return getMinHelper(n -> m_left);
    }
}

// NAIVE MEDIAN: only works if tree is full (balanced)
template <typename T>
T BST<T>::naiveMedian(){
    return m_root -> m_data;
}





// ***************************************************************** // 
// ****************** LECTURE  16 ********************************** // 
// ***************************************************************** // 
// HELPERS FOR REMOVE 
template <typename T>
void BST<T>::findTarget (T key, TreeNode<T>*& target, TreeNode<T>*& parent){
    // find node we want to delete and its parent 
    while (target != NULL && target -> m_data != key){
        // we haven't found target yet
        // set parent = to the current target 
        parent = target; 
        // set target to either left or right child of current target
        if (key <= target -> m_data){
            target = target -> m_left;
        } else {
            target = target -> m_right;
        }
    }
}
template <typename T>
TreeNode<T>* BST<T>::getSuccessor (TreeNode<T>* rightChild){
    while (rightChild -> m_left != NULL){
        rightChild = rightChild -> m_left;
    }
    return rightChild; // is the successor of target, target's rightChild's left most child
}


template <typename T>
void BST<T>::remove(T key){
    // TO DO: check that tree is not empty
    // assume tree is not empty from here on:

    TreeNode<T>* target = NULL; 
    TreeNode<T>* parent = NULL;

    target = m_root;

    // find actual target and parent 
    findTarget(key, target, parent); 

    if (target == NULL){
        // The key does not exist in our tree || the key way not found in our tree. 
        return; // exit method 
    }

    // SCENARIO 1: target has 0 childrent / target is a leaf
    if (target -> m_left == NULL && target -> m_right == NULL){
        if (target == m_root){ // the tree consists of one node and we want to delete it
            m_root = NULL;
        } else { 
            if (target == parent -> m_left){ // target is the left child of parent 
                parent -> m_left = NULL;
            } else { // target is the right child of parent 
                parent -> m_right = NULL;
            }
        }
        delete target; 
        --m_size;
    }

    // SCENARIO 3: target has 2 children 
    else if (target -> m_left != NULL && target -> m_right != NULL){
        // find the successor to replace target
        TreeNode<T>* succ = getSuccessor(target -> m_right);
        T value = succ -> m_data; 
        remove(value); // calls scenario 1 or 2, removes the successor 
        target -> m_data = value;
    }
    // SCENARIO 2: target has 1 child 
    else {
        TreeNode<T>* child; // keep track of target's single child node. 
        // check whether target has a left or right child 
        if (target -> m_left != NULL){ // target has a left child
            child = target -> m_left;
        } else { // target has a right child 
            child = target -> m_right;
        }

        if (target == m_root){
            m_root = child;
        } else {
            if(target == parent -> m_left){ // target is a left child
                parent -> m_left = child; // making the parent's left child the target's child. 
            } else { //the target is a right child. 
                parent -> m_right = child; //making the parent's right child the target's child. 
            }
        }

        target -> m_left = NULL; 
        target -> m_right = NULL; 
        delete target; 
        --m_size;
    }
}

// ***************************************************************** // 
// ****************** LECTURE  17: REMOVE ********************************** // 
// ***************************************************************** // 

template <typename T> 
int BST<T>::maxDepthHelper(TreeNode<T>* subRoot){
    if (subRoot == NULL){
        return 0; // base case
    }
    int leftDepth = maxDepthHelper(subRoot -> m_left);
    int rightDepth = maxDepthHelper(subRoot -> m_right);

    return std::max(leftDepth, rightDepth) + 1;
}

template <typename T> 
int BST<T>::maxDepth(){
    return maxDepthHelper(m_root);
}


#endif

