package util;

import android.util.Log;

public final class Print {

    static String TAG = "com.sourcey.materiallogindemo";

    public static void printError(String text)
    {
        Log.e(TAG,text);
    }
}
