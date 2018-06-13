package com.sourcey.materiallogindemo;

import android.app.ProgressDialog;
import android.content.Intent;
import android.os.Bundle;
import android.support.v7.app.AppCompatActivity;
import android.util.Log;
import android.view.View;
import android.widget.Button;
import android.widget.EditText;
import android.widget.TextView;
import android.widget.Toast;

import com.sourcey.materiallogindemo.util.POSTRequest;
import com.sourcey.materiallogindemo.util.Print;

import java.util.HashMap;
import java.util.UUID;
import java.util.regex.Matcher;
import java.util.regex.Pattern;

import butterknife.BindView;
import butterknife.ButterKnife;

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


        if (!validate()) {
            onSignupFailed();
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

    public boolean validate() {

        boolean value_returned = true;

        if (isEmailValid(email.getText().toString()))
        {

            value_returned = false;
        }

        //TODO finire la funzoipne

        return value_returned;


    }

    public boolean isEmailValid(String email) {
        String expression = "^[\\w\\.-]+@([\\w\\-]+\\.)+[A-Z]{2,4}$";
        Pattern pattern = Pattern.compile(expression, Pattern.CASE_INSENSITIVE);
        Matcher matcher = pattern.matcher(email);
        return matcher.matches();
    }
}