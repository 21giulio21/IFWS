package com.sourcey.materiallogindemo;

import android.app.ProgressDialog;
import android.os.Bundle;
import android.support.v7.app.AppCompatActivity;
import android.view.View;
import android.widget.Button;
import android.widget.EditText;
import android.widget.Toast;

import org.json.JSONException;
import org.json.JSONObject;

import java.util.HashMap;
import java.util.UUID;
import java.util.concurrent.ExecutionException;
import java.util.regex.Matcher;
import java.util.regex.Pattern;

import butterknife.ButterKnife;
import util.POSTRequest;
import util.Print;
import util.UTIL;

public class SignupActivity extends AppCompatActivity {
    private static final String TAG = "SignupActivity";

    EditText email,password,confirm_password;
    Button buttonSingUp;
    ProgressDialog progressDialog;
    
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

                progressDialog = new ProgressDialog(SignupActivity.this,
                        R.style.AppTheme_Dark_Dialog);
                progressDialog.setMessage("Authenticating...");
                progressDialog.show();


                // faccio partire la funzione singup che prevede di registrare l'utente
                new android.os.Handler().postDelayed(
                        new Runnable() {
                            public void run() {
                                try {
                                    signup();
                                } catch (Exception e) {
                                    e.printStackTrace();
                                }

                                progressDialog.dismiss();
                            }
                        }, 3000);


            }
        });


    }

    public void signup() throws ExecutionException, InterruptedException, JSONException {

        buttonSingUp.setEnabled(false);

        // COntrollo che la mail sia valida
        if (!UTIL.isValidEmail(email.getText().toString()))
        {
            Toast.makeText(getApplicationContext(),"Wrong Email format",Toast.LENGTH_LONG).show();
            return;
        }


        // Controllo che la password sia almeno di 8 caratteri
        if (!UTIL.isValidPassword(password.getText().toString()))
        {
            Toast.makeText(getApplicationContext(),"Password 8 caratteri minimo",Toast.LENGTH_LONG).show();
            return;
        }


        // Controllo che la password sia uguale alla conferma Password


        if (!password.getText().toString().equals(confirm_password.getText().toString()))
        {
            Toast.makeText(getApplicationContext(),"Password inserite non coincidono",Toast.LENGTH_LONG).show();
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
        final String ritorno = request.execute(valori).get();

        if(!ritorno.equals("success"))
        {

            new android.os.Handler().postDelayed(
                    new Runnable() {
                        public void run() {
                            progressDialog.dismiss();
                            Toast.makeText(getApplicationContext(),ritorno,Toast.LENGTH_LONG).show();
                            buttonSingUp.setEnabled(true);
                        }
                    }, 3000);

            return;
        }

        new android.os.Handler().postDelayed(
                new Runnable() {
                    public void run() {
                        // On complete call either onLoginSuccess or onLoginFailed
                        onLoginSuccess();
                        // onLoginFailed();
                        progressDialog.dismiss();
                    }
                }, 3000);



    }

    public void onLoginSuccess() {
        buttonSingUp.setEnabled(true);
        finish();
    }


}