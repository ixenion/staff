// creating rotating coins
// create cylinder and rehape it
// create an empty gameObj and make coin the child of this empty gameOj
// reset transform of child and then the parent empty go
// select child coint and disable "Capsule collider"
// add "Sphere collider" to parent, thus we can detect collision with coin
//
using UnityEngine;
using System.Colletions;

public class TestScript : MonoBehaviour
{
	// use once
	void Start ()
	{
		
	}

	// update is called once per frame
	void Update ()
	{

	}

	private void OnCollisionEnter(Collision collision)
	{
		if (collision.gameObject.tag == "Coin")
			Destroy(collision.gameObject);
	}
}
