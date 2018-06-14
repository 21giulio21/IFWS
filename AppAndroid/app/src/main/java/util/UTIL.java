package util;

import java.util.regex.Matcher;
import java.util.regex.Pattern;

public final class UTIL {

    // COntrolla che la mail sia valida,
    public static boolean isValidEmail(String email) {

        if (email.contains("+"))
        {
            return false;

        }

        String expression = "^[\\w\\.-]+@([\\w\\-]+\\.)+[A-Z]{2,4}$";
        Pattern pattern = Pattern.compile(expression, Pattern.CASE_INSENSITIVE);
        Matcher matcher = pattern.matcher(email);
        return matcher.matches();
    }

    //Password di almeno 8 caratteri
    public static boolean isValidPassword(String password) {
        return password.length() > 7;
    }
}
