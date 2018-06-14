package com.sourcey.materiallogindemo;

import android.app.DownloadManager;
import android.app.ProgressDialog;
import android.os.AsyncTask;
import android.os.Bundle;
import android.support.v7.app.AppCompatActivity;
import android.util.Log;

import android.content.Intent;
import android.view.View;
import android.widget.Button;
import android.widget.EditText;
import android.widget.TextView;
import android.widget.Toast;


import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.io.OutputStreamWriter;
import java.io.UnsupportedEncodingException;
import java.net.URL;
import java.net.URLConnection;
import java.net.URLEncoder;
import java.util.HashMap;
import java.util.Map;
import java.util.UUID;
import java.util.concurrent.ExecutionException;

import butterknife.BindView;
import butterknife.ButterKnife;
import util.POSTRequest;
import util.Print;
import util.UTIL;


public class LoginActivity extends AppCompatActivity {


    private static final int REQUEST_SIGNUP = 0;

    @BindView(R.id.input_email) EditText _emailText;
    @BindView(R.id.input_password) EditText _passwordText;
    @BindView(R.id.btn_login) Button _loginButton;
    @BindView(R.id.link_signup) TextView _signupLink;
    
    @Override
    public void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_login);
        ButterKnife.bind(this);


        
        _loginButton.setOnClickListener(new View.OnClickListener() {

            @Override
            public void onClick(View v) {
                try {

                    final String email = _emailText.getText().toString();
                    final String password = _passwordText.getText().toString();

                    login(email,password);
                } catch (UnsupportedEncodingException e) {
                    e.printStackTrace();
                } catch (InterruptedException e) {
                    e.printStackTrace();
                } catch (ExecutionException e) {
                    e.printStackTrace();
                }
            }
        });

        _signupLink.setOnClickListener(new View.OnClickListener() {

            @Override
            public void onClick(View v) {
                // Start the Signup activity
                Intent intent = new Intent(getApplicationContext(), SignupActivity.class);
                startActivityForResult(intent, REQUEST_SIGNUP);
                finish();
                overridePendingTransition(R.anim.push_left_in, R.anim.push_left_out);
            }
        });
    }

    public void login(String email,String password) throws UnsupportedEncodingException, ExecutionException, InterruptedException {

        Print.printError(email);

        // COntrollo che la mail sia valida
        if (!UTIL.isValidEmail(email))
        {
            Toast.makeText(getApplicationContext(),"Wrong Email format",Toast.LENGTH_LONG).show();
            return;
        }

        // Controllo che la password sia almeno di 8 caratteri
        if (!UTIL.isValidPassword(password))
        {
            Toast.makeText(getApplicationContext(),"Password 8 caratteri minimo",Toast.LENGTH_LONG).show();
            return;
        }

        _loginButton.setEnabled(false);

        final ProgressDialog progressDialog = new ProgressDialog(LoginActivity.this,
                R.style.AppTheme_Dark_Dialog);
        progressDialog.setIndeterminate(true);
        progressDialog.setMessage("Authenticating...");
        progressDialog.show();

        // Se sono qui allora devo inserire l'account nel database di altervista
        // Creo la mappa contenete chiave e valore per l'utente che creo
        HashMap<String,String> valori = new HashMap<>();
        valori.put("url",getResources().getString(R.string.url_login_user));
        valori.put("email",email);
        valori.put("password",password);

        POSTRequest request = new POSTRequest();
        final String ritorno = request.execute(valori).get();

        if(!ritorno.equals("success"))
        {

            new android.os.Handler().postDelayed(
                    new Runnable() {
                        public void run() {
                            progressDialog.dismiss();
                            Toast.makeText(getApplicationContext(),ritorno,Toast.LENGTH_LONG).show();
                            _loginButton.setEnabled(true);
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


    @Override
    protected void onActivityResult(int requestCode, int resultCode, Intent data) {
        if (requestCode == REQUEST_SIGNUP) {
            if (resultCode == RESULT_OK) {
                this.finish();
            }
        }
    }

    @Override
    public void onBackPressed() {
        // Disable going back to the MainActivity
        moveTaskToBack(true);
    }

    public void onLoginSuccess() {
        _loginButton.setEnabled(true);
        finish();
    }











}
