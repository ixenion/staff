using UnityEngine;
using System.Colletions;

public class TestScript : MonoBehaviour
{	
	Rigidbody rb;

	public int a;
	private int b;
	
	// used once at start
	// but even if the script is deactivated
	void Awake ()
	{
		Debug.Log ("inside Awake");
		// destroy game object to whih this script attached immideately
		Destroy(gameobject);
		// after 3 sec
		Destroy(gameObject, 3f);
	}

	// use once
	// and only if the script is activated (checkbox)
	void Start ()
	{
		// shows debug info in console menu
		Debug.Log ("inside Start");
		// usage of funtions (methods)
		Shoot (5);
		int a = Jump (10);
		// destroy object atteched after 3 seconds
		Destroy (gameObject,3f);

		rb = GetComponent<Rigidbody>();

	}

	// update is called once per frame
	void Update ()
	{
		// key input
		if (Input.GetKeyDown(KeyCode.Space)){
			//Destroy(gameObject);
			// add force
			rb.AddForce(Vector3.up * 500);
			// or add velocity
			rb.velocity = Vector3.forward * 20f;
	}
	
	// no return
	void Shoot (int data)
	{
		Debug.Log ("Shooting!!!!");
		Debug.Log ("data");
	}

	// with return
	int Jump (int beta)
	{
		Debug.Log("beta");
		return (beta + 5);
	}

	private void OnMouseDown()
	{
		Destroy(gameObject);// destroes gO by licking on it
	}

	private void OnCollisionEnter(Collision collision){
		if (collision.gameObject.tag == "Enemy"){
			Destroy(gameObject);// destroy gameObject, not Enemy
			Destroy(col.gameObject);// destroy Enemy
		}
	}
			
}
