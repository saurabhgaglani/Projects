using UnityEngine.SceneManagement;
using UnityEngine;

public class GameOverScript : MonoBehaviour
{

    public void Setup()
    {
        gameObject.SetActive(true);
    }

    public void RestartButton()
    {
        SceneManager.LoadScene(SceneManager.GetActiveScene().name);
    }
}
