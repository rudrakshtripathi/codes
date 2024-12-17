public class GCDOfStrings {
     static void main(String[] args) {
        String str1 = "ABCDABCD";
        String str2 = "ABCD";
        System.out.println("GCD of Strings: " + gcdOfStrings(str1, str2));
    }

    public static String gcdOfStrings(String str1, String str2) {
        // If one of the strings is empty, return the other string
        if (str1.isEmpty()) return str2;
        if (str2.isEmpty()) return str1;

        // If the strings are not equal, we need to find the substring that can divide both
        if (str1.length() > str2.length()) {
            if (str1.startsWith(str2)) {
                return gcdOfStrings(str1.substring(str2.length()), str2);
            } else {
                return "";
            }
        } else {
            if (str2.startsWith(str1)) {
                return gcdOfStrings(str1, str2.substring(str1.length()));
            } else {
                return "";
            }
        }
    }
}
