// trigger used as checkpoints. Collide alert is happening ut no physical ollision
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

	void OnTriggerEnter2D(Collider2D col)
	{
		if (col.gameObject.tag == "someTag")
			Destroy (col.gameObject);
	}
}
