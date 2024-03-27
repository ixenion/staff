using UnityEngine;
using System.Colletions;

public class TestScript : MonoBehaviour
{
	GameObject Raja;
	GameObject[] Ali;
	// use once
	void Start ()
	{
		if (this.gameObjet.tag == "quad")
		{
			Debug.Log ("It's a quad");
		}

		// find and destroy specific (one) object by tag
		Raja = GameObject.FindWithTag ("Raja");
		Destroy (Raja);
		
		// find and distroy multiple objects y tag
		Ali = GameObject.FindGameObjectsWithTag ("Ali");
		foreach (GameObject a in Ali){
			Destroy (a.GameObject);
		
		}
	}

	// update is called once per frame
	void Update ()
	{

	}
}
