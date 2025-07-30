import java.util.Random;
public class randomMatrix{
   public static int[][] randomMatrix(int rows, int columns) {
      int[][] matrix = new int[rows][columns];
      Random random = new Random();

      for (int i = 0; i < rows; i++) {
         for (int j = 0; j < columns; j++) {
            matrix[i][j] = random.nextInt(9);
         }
      }

      return matrix;
   }

public static void printMatrix(int[][] matrix) {
      for (int i = 0; i < matrix.length; i++) {
         for (int j = 0; j < matrix[0].length; j++) {
            System.out.print(matrix[i][j] + " ");
         }
         System.out.println();
      }
   }

public static void main(String[] args) {
      int rows = 3;
      int columns = 4;

      int[][] randomMatrix = randomMatrix(rows, columns);

      System.out.println("Random Matrix:");
      printMatrix(randomMatrix);
   }
}
