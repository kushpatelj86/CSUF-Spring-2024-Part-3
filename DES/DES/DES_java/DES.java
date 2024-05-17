/**
 * Demo of DES encryption in Java.
 * Some materials borrowed from 
 * http://www.mkyong.com/java/jce-encryption-data-encryption-standard-des-tutorial/
 */

import java.security.InvalidKeyException;
import java.security.NoSuchAlgorithmException;
 
import javax.crypto.BadPaddingException;
import javax.crypto.Cipher;
import javax.crypto.IllegalBlockSizeException;
import javax.crypto.KeyGenerator;
import javax.crypto.NoSuchPaddingException;
import java.security.spec.InvalidKeySpecException;
import javax.crypto.SecretKey;
import javax.crypto.SecretKeyFactory;
import javax.crypto.spec.DESKeySpec;
 
public class DES
{    
	public static void main(String[] argv) 
	{
 
		try{
 
		    /**
		      * Create an instance of a key generator; a class used
		      * for generating DES encryption keys.
		      */
		    KeyGenerator keygenerator = KeyGenerator.getInstance("DES");
		   
		    /**
		     * Generate a DES key
		     */
		    SecretKey myDesKey = keygenerator.generateKey();
			
		    /**
 		      * NOTE: the above will generate a random key.
		      * You can also specify your own key as follows:
		      * (please feel free to uncomment the play around)
		      */

	//	    SecretKeyFactory secretKeyFactory = SecretKeyFactory.getInstance("DES");
        //
        //        try
	//	    {
	//		    myDesKey = secretKeyFactory.generateSecret(new DESKeySpec(
	//				new byte[] {0x11,0x21,0x31,0x41,0x51,0x61,0x71,(byte) 0x81}));
	//	    }
	//	    catch(InvalidKeySpecException e)		
	//	    {
	//		    e.printStackTrace();
	//	    }

		    /* Create an instance of the DES cipher */
		    Cipher desCipher = Cipher.getInstance("DES/ECB/PKCS5Padding");
 
		    /* Initialize the cipher for encryption. */
		    desCipher.init(Cipher.ENCRYPT_MODE, myDesKey);
 
		    /* Plaintext which we would like to encrypt */
		    byte[] plainText = "No body can see me".getBytes();
 
		    System.out.println("Text : " + new String(plainText));
		    System.out.println("Text [Byte Format] : " + plainText);
 
		    /* Encrypt the text */
		    byte[] textEncrypted = desCipher.doFinal(plainText);
 
		    System.out.println("Text Encryted : " + textEncrypted);
 
		    /* Initialize the same cipher for decryption. */
		    desCipher.init(Cipher.DECRYPT_MODE, myDesKey);
 
		    /* Decrypt the text */
		    byte[] textDecrypted = desCipher.doFinal(textEncrypted);
 
		    System.out.println("Text Decryted : " + new String(textDecrypted));
 
		}catch(NoSuchAlgorithmException e){
			e.printStackTrace();
		}catch(NoSuchPaddingException e){
			e.printStackTrace();
		}catch(InvalidKeyException e){
			e.printStackTrace();
		}catch(IllegalBlockSizeException e){
			e.printStackTrace();
		}catch(BadPaddingException e){
			e.printStackTrace();
		} 
 
	}
}
