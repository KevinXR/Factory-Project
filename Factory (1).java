import java.util.ArrayList;
import java.util.List;
import java.util.Scanner;
import java.lang.Math;

public class CodeTranslation {
    public static void main(String[] args) {
        System.out.println("\n┏┳┓┓     ┏��     ┏┓┏  ┏┳┓┓     ┏┓          ");
        System.out.println(" ┃ ┣┓┏┓  ┣┫┏┓╋  ┃┃╋   ┃ ┣┓┏┓  ┣ ┏┓┏╋┏┓┏┓┓┏");
        System.out.println(" ┻ ┛┗┗   ┛┗┛ ┗  ┗┛┛   ┻ ┛���┗   ┻ ┗┻┗┗┗��┛ ┗┫");
        System.out.println("━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ ");
        System.out.println("                                             ");

        List<Object> list = new ArrayList<>();
        list.add("none");
        list.add(2);
        list.add("none");
        list.add("yes");
        list.add(0.0);
        list.add(51);

        options();
    }

    public static void basic(List<Object> array) {
        String ideology = (String) array.get(0);
        int factory = (int) array.get(1);
        String decide = (String) array.get(2);
        String corrupt = (String) array.get(3);
        double extra = (double) array.get(4);
        int city = (int) array.get(5);

        int steel = 3;
        int elect = 16;
        int fert = 12;
        int motor = 6;
        int civ = 40;
        double x = city * 2.5;
        double y = city * 3;
        int m = (int) Math.ceil(x / motor);
        int e = (int) Math.ceil(y / elect);
        int f = (int) Math.ceil(x / fert);
        int s = (int) Math.ceil(motor / steel);
        double factory1 = .2;
        double factory2 = .45;
        double factory3 = .7;
        double factory4 = 1.2;
        double factory5 = 1.7;
        double communist = 2.25;
        double socialist = 1.5;
        double forced = .4;
        double public = .2;
        double sinola = .35;
        double modifier = 1.00;

        if (ideology.equals("communism")) {
            steel = (int) (steel * communist);
            elect = (int) (elect * communist);
            motor = (int) (motor * communist);
            fert = (int) (fert * communist);
            civ = (int) (civ * communist);
        } else if (ideology.equals("socialism")) {
            steel = (int) (steel * socialist);
            elect = (int) (elect * socialist);
            motor = (int) (motor * socialist);
            fert = (int) (fert * socialist);
            civ = (int) (civ * socialist);
        }
        System.out.println("");
        if (factory == 1) {
            modifier = modifier + factory1;
        } else if (factory == 2) {
            modifier = modifier + factory2;
        } else if (factory == 3) {
            modifier = modifier + factory3;
        } else if (factory == 4) {
            modifier = modifier + factory4;
        } else if (factory == 5) {
            modifier = modifier + factory5;
        } else {
            modifier = modifier + 0;
        }
        if (corrupt.equals("yes")) {
            modifier = modifier + sinola;
        } else {
            modifier = modifier + 0;
        }
        System.out.println("-----------------------------------------------------------------");
        if (decide.equals("forced labor")) {
            modifier = modifier + forced;
        } else if (decide.equals("public service")) {
            modifier = modifier + public;
        } else if (decide.equals("both")) {
            modifier = modifier + public + forced;
        } else {
            modifier = modifier + 0;
        }
        System.out.println("");

        modifier = modifier + (extra / 100);
        double m2 = x / (motor * modifier);
        double f2 = x / (fert * modifier);
        double e2 = y / (elect * modifier);
        double s2 = m2 / (steel * modifier);
        int m3 = (int) Math.ceil(m2);
        int f3 = (int) Math.ceil(f2);
        int e3 = (int) Math.ceil(e2);
        int s3 = (int) Math.ceil(s2);
        double mr = (m3 * 2) + .1;
        double fr = (f3 * 3.5) + .1;
        double er = (e3 * 2) + .1;
        double sr = (s3 * 4) + .1;
        double sr2 = (s3 * 0.2) + .1;
        double income = (m3 + e3 + f3 + s3 + city) * 250000;
        double dif = (mr * 96000 + er * 96000 + fr * 41500 + sr * 38000 + sr2 * 102000);

        System.out.println("Motor factory makes about: " + String.format("%.2f", (motor * modifier)) + " motor parts");
        System.out.println("Electronics factory makes about: " + String.format("%.2f", (elect * modifier)) + " electronics");
        System.out.println("Fertilizer factory makes about: " + String.format("%.2f", (fert * modifier)) + " fertilizers");
        System.out.println("Steel factory makes about: " + String.format("%.2f", (steel * modifier)) + " steel");
        System.out.println("Civilian factory makes about: " + String.format("%.2f", (civ * modifier)) + " consumer goods");
        System.out.println("Cost to build everything: " + String.format("%,.0f", (25000000 * ((m3 + f3 + e3 + s3) + city))));
        System.out.println("\nYou need: \n" + m3 + " motor factories \n" + e3 + " electronic factories \n" + f3 + " fertilizer factories \n" + s3 + " steel factories \n");
        System.out.println("Resources you need: \n" + mr + " Tungsten \n" + er + " Copper and Gold \n" + fr + " Phosphate \n" + sr + " Iron \n" + String.format("%.2f", sr2) + " Titanium \n");
        System.out.println("Good luck LMAO");
        System.out.println("Your resource income is: " + String.format("%,.0f", income));
        System.out.println("Your actual income is: " + String.format("%,.0f", (income - dif)));
    }

    public static void test() {
        List<Object> list = new ArrayList<>();
        list.add("none");
        list.add(2);
        list.add("none");
        list.add("yes");
        list.add(0.0);
        list.add(51);
        basic(list);
    }

    public static void getMods() {
        Scanner scanner = new Scanner(System.in);
        System.out.println("\nIdeology? ");
        String ideology = scanner.nextLine();

        System.out.println("Factory output? (0-5) ");
        int factory = scanner.nextInt();

        scanner.nextLine();
        System.out.println("What policy? (forced labor, public service, both or none)");
        String decide = scanner.nextLine();

        System.out.println("Do you have Ignore safety Regulations? (Yes/No)");
        String corrupt = scanner.nextLine();

        System.out.println("Enter any custom factory modifiers in a percentage. Put 0 if there are none. (25% = 25) ");
        double extra = scanner.nextDouble();

        System.out.println("Civilian factory count? ");
        int city = scanner.nextInt();

        List<Object> list = new ArrayList<>();
        list.add(ideology);
        list.add(factory);
        list.add(decide);
        list.add(corrupt);
        list.add(extra);
        list.add(city);
    }

    public static void options() {
        Scanner scanner = new Scanner(System.in);
        int option = 0;
        while (option != 5) {
            System.out.println("Enter the number associated with the action: \n");
            System.out.println("(1) Factory spam!");
            System.out.println("(2) Resource policies");
            System.out.println("(3) How many factories do I need for X amount of Y");
            System.out.println("(4) Change modifiers");
            System.out.println("(5) Return to menu");
            option = scanner.nextInt();
            if (option == 1) {
                List<Object> list = new ArrayList<>();
                list.add("none");
                list.add(2);
                list.add("none");
                list.add("yes");
                list.add(0.0);
                list.add(51);
                basic(list);
                System.out.println("-----------------------------------------------------------------");
            } else if (option == 2) {
                System.out.println(2);
                System.out.println("-----------------------------------------------------------------");
            } else if (option == 3) {
                System.out.println(3);
                System.out.println("-----------------------------------------------------------------");
            } else if (option == 4) {
                getMods();
                System.out.println("-----------------------------------------------------------------");
            } else if (option == 5) {
                System.out.println("You have returned to menu.");
            } else {
                System.out.println("Invalid input, please try again");
            }
        }
    }
}


