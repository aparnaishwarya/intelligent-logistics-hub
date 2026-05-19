import java.io.FileWriter;
import java.io.IOException;
import java.util.ArrayList;

public class InventoryService {

    private ArrayList<Product> products = new ArrayList<>();

    // Add product
    public void addProduct(Product product) {
        products.add(product);
        System.out.println("Product added successfully!");
    }

    // View products
    public void viewProducts() {

        if (products.isEmpty()) {
            System.out.println("Inventory is empty.");
            return;
        }

        System.out.println("\n===== PRODUCT LIST =====");

        for (Product product : products) {
            System.out.println(product);
        }
    }

    // Update stock
    public void updateStock(int id, int newQuantity) {

        for (Product product : products) {
            if (product.getId() == id) {
                product.setQuantity(newQuantity);
                System.out.println("Stock updated successfully!");
                return;
            }
        }

        System.out.println("Product not found.");
    }

    // Delete product
    public void deleteProduct(int id) {

        for (int i = 0; i < products.size(); i++) {
            if (products.get(i).getId() == id) {
                products.remove(i);
                System.out.println("Product deleted successfully!");
                return;
            }
        }

        System.out.println("Product not found.");
    }

    // Save inventory to file
    public void saveToFile() {

        try {

            FileWriter writer = new FileWriter("../data/inventory.txt");

            for (Product product : products) {
                writer.write(product.toString() + "\n");
            }

            writer.close();

            System.out.println("Inventory saved to file.");

        } catch (IOException e) {
            System.out.println("Error saving file: " + e.getMessage());
        }
    }
}