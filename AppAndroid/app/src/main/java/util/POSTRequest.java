package util;


import android.os.AsyncTask;

import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.io.OutputStreamWriter;
import java.io.UnsupportedEncodingException;
import java.net.URL;
import java.net.URLConnection;
import java.net.URLEncoder;
import java.util.HashMap;

public class POSTRequest extends AsyncTask<HashMap<String,String>, Void, String> {

    @Override
    protected String doInBackground(HashMap<String, String>... hashMaps){

        String url = hashMaps[0].remove("url");
        Object keys [] = hashMaps[0].keySet().toArray();

        String data = "";

        if (keys.length == 1)
        {
            try {
                data = URLEncoder.encode(keys[0].toString(), "UTF-8")
                            + "=" + URLEncoder.encode(hashMaps[0].get(keys[0].toString()), "UTF-8");
            } catch (UnsupportedEncodingException e) {
                e.printStackTrace();
            }

        }else {

            try {
                data = URLEncoder.encode(keys[0].toString(), "UTF-8")
                        + "=" + URLEncoder.encode(hashMaps[0].get(keys[0].toString()), "UTF-8");

            } catch (UnsupportedEncodingException e) {
                e.printStackTrace();
            }
            for(int j = 1; j <keys.length; j++)
            {
                try {
                    data += "&" + URLEncoder.encode(keys[j].toString(), "UTF-8") + "="
                            + URLEncoder.encode(hashMaps[0].get(keys[j].toString()), "UTF-8");
                } catch (UnsupportedEncodingException e) {
                    e.printStackTrace();
                }

            }




        }

        String text = "";
        BufferedReader reader=null;

        // Send data
        try
        {

            // Defined URL  where to send data
            URL url_url = new URL(url);

            // Send POST data request

            URLConnection conn = url_url.openConnection();
            conn.setDoOutput(true);
            OutputStreamWriter wr = new OutputStreamWriter(conn.getOutputStream());
            wr.write( data );
            wr.flush();

            // Get the server response

            reader = new BufferedReader(new InputStreamReader(conn.getInputStream()));
            StringBuilder sb = new StringBuilder();
            String line = null;

            // Read Server Response
            while((line = reader.readLine()) != null)
            {
                // Append server response in string
                sb.append(line + "\n");
            }


            text = sb.toString();
            Print.printError(text);
        }
        catch(Exception ex)
        {
            ex.printStackTrace();
        }



        return null;
    }




}