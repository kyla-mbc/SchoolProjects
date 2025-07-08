import java.util.Random;
public class MatrixExample{
    // ACTIVITY: randomMatrix

    // ACTIVITY: rowSums
    
    // IN CLASS: printArray
    public static void printArray(int[] a){
        // System.out.println(a); // remember that this only prints memory address
        for (int idx = 0; idx < a.length; ++idx){
            System.out.println(a[idx]);
        }
    }

    public static void printArray(double[] a){
        // System.out.println(a); // remember that this only prints memory address
        for (int idx = 0; idx < a.length; ++idx){
            System.out.println(a[idx]);
        }
    }

    public static void printArray(String[] a){
        // System.out.println(a); // remember that this only prints memory address
        for (int idx = 0; idx < a.length; ++idx){
            System.out.println(a[idx]);
        }
    }

    // IN CLASS: printMatrix
    public static void printMatrix(int[][] m){
        for (int rowIdx = 0; rowIdx < m.length; ++rowIdx){
            for (int colIdx = 0; colIdx < m[0].length; ++colIdx){
                System.out.print(m[rowIdx][colIdx] + "\t");
            }
            System.out.println();
        }
    }

    public static void printMatrix(double[][] m){
        for (int rowIdx = 0; rowIdx < m.length; ++rowIdx){
            for (int colIdx = 0; colIdx < m[0].length; ++colIdx){
                System.out.print(m[rowIdx][colIdx] + "\t");
            }
            System.out.println();
        }
    }

    public static void printMatrix(String[][] m){
        for (int rowIdx = 0; rowIdx < m.length; ++rowIdx){
            for (int colIdx = 0; colIdx < m[0].length; ++colIdx){
                System.out.print(m[rowIdx][colIdx] + "\t");
            }
            System.out.println();
        }
    }

    public static void main(String[] args){
        // ONE-DIMENSIONAL ARRAY
        // Allocate memory / create the array 
        // double[] dblArr = new double[5];
        // printArray(dblArr);
        // populate the array with some numbers 

        // 2-D ARRAY / MATRIX
        // Allocate memory / create the array 
        int[][] myMatrix = new int[5][13];
        // populate the array with some numbers 
        for (int rowIdx = 0; rowIdx < myMatrix.length; ++rowIdx){
            for (int colIdx = 0; colIdx < myMatrix[0].length; ++colIdx){
                myMatrix[rowIdx][colIdx] = rowIdx * colIdx;
            }
        }
        
        printMatrix(myMatrix);


        // ACTIVITY: Calling the methods 
        // create random matrix:
        // int[][] myMatrix = randomMatrix(2, 3);
        // sum rows of matrix 
        // int[] myMatrixRowSums = rowSums(myMatrix);
        // print original matrix and results:
        // System.out.println("Original random matrix: ");
        // printMatrix(myMatrixRowSums);
        // System.out.println("Sum of rows of random matrix: ");
        // printArray(myMatrixRowSums);

    }

}