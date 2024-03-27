// create 2 scines - Level1 and Level2
// create ui label with text "Level1" at Level1 with pos x,y,z = 0;
// create ui label with text "Level2" at Level2 with pos x,y,z = 0;
// create empty object and name it SceneLoader
// into that create SceneLoaderScript
// and fill it with next script
// meanwhile file -> Build settings -> drag and drop sccenes to "scenes in build". To the right would be scenes indexes (0 and 1)
//
using UnityEngine;
using System.Colletions;
using UnityEngine.sceneManagment;

public class TestScript : MonoBehaviour
{
	// use once
	void Start ()
	{
		
	}

	// update is called once per frame
	void Update ()
	{
		if (Input.GetKeyDown(KeyCode.Space)){
			// load level
			//Aplication.LoadLevel("Level2")
			SceneManager.LoadScene (1);
			//SceneManager.LoadScene ("Level2");
			//SceneManager.LoadScene (1, LoadSceneMode.Additive);// load  2 scenes at a same time
		}
	}
}
