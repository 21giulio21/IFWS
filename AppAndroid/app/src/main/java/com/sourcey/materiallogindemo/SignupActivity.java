package com.sourcey.materiallogindemo;

import android.os.Bundle;
import android.support.v7.app.AppCompatActivity;
import android.view.View;
import android.widget.Button;
import android.widget.EditText;
import android.widget.Toast;

import java.util.HashMap;
import java.util.UUID;
import java.util.regex.Matcher;
import java.util.regex.Pattern;

import butterknife.ButterKnife;
import util.POSTRequest;
import util.Print;

public class SignupActivity extends AppCompatActivity {
    private static final String TAG = "SignupActivity";

    EditText email,password,confirm_password;
    Button buttonSingUp;

    
    @Override
    public void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_signup);
        ButterKnife.bind(this);

        email = (EditText) findViewById(R.id.email);
        password = (EditText) findViewById(R.id.password);
        confirm_password = (EditText) findViewById(R.id.confirm_passwprd);
        buttonSingUp = (Button) findViewById(R.id.btn_signup);
        buttonSingUp.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View v) {
                Print.printError(email.getText().toString());
                Print.printError(password.getText().toString());
                Print.printError(confirm_password.getText().toString());

                signup();
            }
        });


    }

    public void signup() {

        if (!isEmailValid(email.getText().toString()))
        {
            Toast.makeText(getApplicationContext(),"Wrong Email format",Toast.LENGTH_LONG).show();
            return;
        }





        // Se sono qui allora devo inserire l'account nel database di altervista
        // Creo la mappa contenete chiave e valore per l'utente che creo
        HashMap<String,String> valori = new HashMap<>();
        valori.put("url",getResources().getString(R.string.url_register_user));
        valori.put("email",email.getText().toString());
        valori.put("password",password.getText().toString());
        valori.put("username_instagram", UUID.randomUUID().toString());

        POSTRequest request = new POSTRequest();
        request.execute(valori);



    }


    public void onSignupSuccess() {

    }

    public void onSignupFailed() {

    }


    // COntrolla che la mail sia valida,
    public boolean isEmailValid(String email) {

        if (email.contains("+"))
        {
            return false;

        }

        String expression = "^[\\w\\.-]+@([\\w\\-]+\\.)+[A-Z]{2,4}$";
        Pattern pattern = Pattern.compile(expression, Pattern.CASE_INSENSITIVE);
        Matcher matcher = pattern.matcher(email);
        return matcher.matches();
    }
}