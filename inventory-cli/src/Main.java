import java.util.Scanner;

public class Main {

    public static void main(String[] args) {

        Scanner scanner = new Scanner(System.in);

        InventoryService service = new InventoryService();

        int choice = 0;

        do {

            System.out.println("\n===== INVENTORY MANAGEMENT =====");

            System.out.println("1. Add Product");
            System.out.println("2. View Products");
            System.out.println("3. Update Stock");
            System.out.println("4. Delete Product");
            System.out.println("5. Save Inventory");
            System.out.println("6. Exit");

            System.out.print("Choose option: ");

            String input = scanner.nextLine().trim();

            if (input.isEmpty()) {
                continue;
            }

            try {

                choice = Integer.parseInt(input);

            } catch (NumberFormatException e) {

                System.out.println("Please enter a valid number.");
                continue;
            }

            switch (choice) {

                case 1:

                    try {

                        System.out.print("Enter Product ID: ");
                        int id =
                                Integer.parseInt(scanner.nextLine());

                        System.out.print("Enter Product Name: ");
                        String name = scanner.nextLine();

                        System.out.print("Enter Product Price: ");
                        double price =
                                Double.parseDouble(scanner.nextLine());

                        System.out.print("Enter Quantity: ");
                        int quantity =
                                Integer.parseInt(scanner.nextLine());

                        Product product =
                                new Product(id, name, price, quantity);

                        service.addProduct(product);

                    } catch (NumberFormatException e) {

                        System.out.println(
                                "Invalid input. Please enter correct values."
                        );
                    }

                    break;

                case 2:

                    service.viewProducts();

                    break;

                case 3:

                    try {

                        System.out.print("Enter Product ID: ");
                        int updateId =
                                Integer.parseInt(scanner.nextLine());

                        System.out.print("Enter New Quantity: ");
                        int newQty =
                                Integer.parseInt(scanner.nextLine());

                        service.updateStock(updateId, newQty);

                    } catch (NumberFormatException e) {

                        System.out.println(
                                "Invalid input. Please enter numbers only."
                        );
                    }

                    break;

                case 4:

                    try {

                        System.out.print("Enter Product ID: ");
                        int deleteId =
                                Integer.parseInt(scanner.nextLine());

                        service.deleteProduct(deleteId);

                    } catch (NumberFormatException e) {

                        System.out.println(
                                "Invalid input. Please enter numbers only."
                        );
                    }

                    break;

                case 5:

                    service.saveToFile();

                    break;

                case 6:

                    System.out.println("Exiting program...");

                    break;

                default:

                    System.out.println("Invalid choice.");
            }

        } while (choice != 6);

        scanner.close();
    }
}