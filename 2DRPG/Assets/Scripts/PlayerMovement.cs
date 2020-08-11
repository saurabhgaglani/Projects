using UnityEngine;

public class PlayerMovement : MonoBehaviour
{

    public float moveSpeed; 
    private Animator anim;
    private bool IsMoving;
    private Vector2 MoveDir;

    // Start is called before the first frame update
    void Start()
    {

        anim = GetComponent<Animator>();
        
    }

    // Update is called once per frame
    void Update()
    {
        IsMoving = false;

        if(Input.GetAxisRaw("Horizontal")>0 || Input.GetAxisRaw("Horizontal")<0 )
        {
            transform.Translate(new Vector3(Input.GetAxisRaw("Horizontal") * moveSpeed *Time.deltaTime, 0f, 0f));
            MoveDir = new Vector2(Input.GetAxisRaw("Horizontal"), 0f);
            IsMoving = true;
        }

        else if(Input.GetAxisRaw("Vertical")<0 || Input.GetAxisRaw("Vertical")>0  )
        {
            transform.Translate(new Vector3(0f, Input.GetAxisRaw("Vertical") * moveSpeed *Time.deltaTime, 0f));
            MoveDir = new Vector2(0f, Input.GetAxisRaw("Vertical"));
            IsMoving = true;
        }



        anim.SetFloat("MoveX", Input.GetAxisRaw("Horizontal"));
        anim.SetFloat("MoveY", Input.GetAxisRaw("Vertical"));
        anim.SetBool("PlayerMoving", IsMoving);
        anim.SetFloat("LastMoveX", MoveDir.x);
        anim.SetFloat("LastMoveY", MoveDir.y);

    
    }
}
