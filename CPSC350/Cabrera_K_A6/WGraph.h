// Full name: Kyla Monique Cabrera
// Student ID: 2445213
// Chapman Email: kycabrera@chapman.edu
// Course number and section: CPSC-350-03
// Assignment: Programming Assignment 6 - Kruzkal's

#ifndef WGRAPH_H
#define WGRAPH_H

#include <iostream>
#include <vector>
#include <queue>
#include <set> // Used to keep track of nodes/edges added to the MST
#include <unordered_map> // Used for key-value mappings
#include <limits> // For numeric limits to indicate infinity
#include <tuple>  // For storing edges as (weight, node1, node2)
#include <iomanip> // Used for formatting input and outputs


// Class to represent each vertex
template <typename T>
class Vertex {
public:
    T name; 
    Vertex(T n); // Constructor
    ~Vertex(); // Destructor
};

template <typename T>
Vertex<T>::Vertex(T n) {name = n;} // Assign 'name' during construction

template <typename T>
Vertex<T>::~Vertex() {}

// Class to represent a weighted graph
template <typename T>
class WGraph {
public:
    WGraph(int s); // Constructor to initialize graph of a given size
    ~WGraph(); // Destructor to clean up dynamic allocations

    void addVertex(T name); // Add a vertex to the graph
    void addEdge(T name1, T name2, double weight); // Add an edge between two vertices with a weight
    void computeMST(); // Computes the MST using Kruskal's algorithm

private:
    int m_size; // Maximum number of vertices in the graph
    double** m_adj; // 2D array representing adjacency matrix for edge weights
    std::vector<Vertex<T>> m_vertices; // List of vertices
    std::unordered_map<T, int> m_nameToIndex; // Map to track each vertex's index by name

    // Helper functions for union-find
    int findParent(std::vector<int>& parent, int node); // Find the parent of a node
    void unionNodes(std::vector<int>& parent, std::vector<int>& rank, int node1, int node2); // Union two sets
};

// Constructor
template <typename T>
WGraph<T>::WGraph(int s) {
    m_size = s;
    m_adj = new double*[m_size]; // Allocate memory for adjacency matrix
    for (int i = 0; i < m_size; ++i) {
        m_adj[i] = new double[m_size];
        for (int j = 0; j < m_size; ++j) {
            m_adj[i][j] = std::numeric_limits<double>::max(); // Initialize with infinity
        }
    }
}

// Destructor
template <typename T>
WGraph<T>::~WGraph() {
    for (int i = 0; i < m_size; ++i) {
        delete[] m_adj[i]; // Deallocate row memory
    }
    delete[] m_adj; // Deallocate matrix memory
}

// Add a new vertex to the graph
template <typename T>
void WGraph<T>::addVertex(T name) {
    if (m_vertices.size() < m_size) {
        m_vertices.push_back(Vertex<T>(name)); // Add vertex to the list
        m_nameToIndex[name] = m_vertices.size() - 1; // Map the vertex name to its index
    } else {
        std::cout << "Graph capacity reached. Cannot add more vertices." << std::endl;
    }
}

// Add an edge with a weight between two vertices
template <typename T>
void WGraph<T>::addEdge(T name1, T name2, double weight) {
    if (m_nameToIndex.count(name1) > 0 && m_nameToIndex.count(name2) > 0) {
        int i = m_nameToIndex[name1];
        int j = m_nameToIndex[name2];
        m_adj[i][j] = weight; // Set edge weight in adjacency matrix
        m_adj[j][i] = weight; // Symmetric for undirected graph
    } else {
        std::cout << "One or both vertices not found in the graph." << std::endl;
    }
}

// Compute MST
template <typename T>
void WGraph<T>::computeMST() {
    using Edge = std::tuple<double, int, int>; // Represent edges as (weight, node1, node2)
    std::priority_queue<Edge, std::vector<Edge>, std::greater<Edge>> edgeQueue;

    // Collect all edges from the adjacency matrix
    for (int i = 0; i < m_size; ++i) {
        for (int j = i + 1; j < m_size; ++j) {
            if (m_adj[i][j] != std::numeric_limits<double>::max()) { // Ignore infinite weights
                edgeQueue.push(std::make_tuple(m_adj[i][j], i, j)); // Push edge into priority queue
            }
        }
    }

    // Initialize union-find structures for MST
    std::vector<int> parent(m_size), rank(m_size, 0);
    for (int i = 0; i < m_size; ++i) {
        parent[i] = i; // Each node is initially its own parent
    }

    // MST variables
    double mstCost = 0; // Total cost of the MST
    std::vector<std::vector<double>> mstMatrix(m_size, std::vector<double>(m_size, 0)); // Adjacency matrix for MST
    int edgeCount = 0; // Count of edges in MST

    // Process edges in increasing order of weight
    while (!edgeQueue.empty() && edgeCount < m_size - 1) {
        Edge edge = edgeQueue.top(); // Get the edge with the smallest weight
        edgeQueue.pop();
        double weight = std::get<0>(edge);
        int u = std::get<1>(edge);
        int v = std::get<2>(edge);

        // Check if adding this edge creates a cycle
        if (findParent(parent, u) != findParent(parent, v)) {
            mstCost += weight; // Add weight to MST cost
            mstMatrix[u][v] = weight; // Add edge to MST adjacency matrix
            mstMatrix[v][u] = weight;
            edgeCount++;
            unionNodes(parent, rank, u, v); // Union the sets
        }
    }

    // Output the MST results
    std::cout << std::fixed << std::setprecision(1); // Set floating-point precision
    std::cout << "The MST Cost is: " << mstCost << "\n";
    for (const auto& row : mstMatrix) {
        for (double val : row) {
            if (val != 0) {
                std::cout << val << " ";
            } else {
                std::cout << "0.0 "; // Format zeros as floats
            }
        }
        std::cout << "\n";
    }
}

// Helper function to find the parent of a node
template <typename T>
int WGraph<T>::findParent(std::vector<int>& parent, int node) {
    if (parent[node] != node) {
        parent[node] = findParent(parent, parent[node]); // Path compression
    }
    return parent[node];
}

// Helper function to ensure a union of two nodes by rank
template <typename T>
void WGraph<T>::unionNodes(std::vector<int>& parent, std::vector<int>& rank, int node1, int node2) {
    int root1 = findParent(parent, node1);
    int root2 = findParent(parent, node2);

    // Union by rank
    if (root1 != root2) {
        if (rank[root1] > rank[root2]) {
            parent[root2] = root1;
        } else if (rank[root1] < rank[root2]) {
            parent[root1] = root2;
        } else {
            parent[root2] = root1;
            rank[root1]++;
        }
    }
}

#endif