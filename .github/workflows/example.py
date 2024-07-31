import os

def main():
  print("Hello from GitHub Actions!")
  print(f'::set-output name=bbb::567')
  token = os.environ.get("AZURE_SECRET_TOKEN")
  if not token:
    raise RuntimeError("AZURE_SECRET_TOKEN env var is not set!")
  print("All good! we found our env var")
  
  with open('.github/workflows/params.json') as f:
    data = json.load(f)
    istl_in_e1 = data[0]['install_e1']
    istl_in_e2 = data[0]['install_e2']
    istl_in_e3 = data[0]['install_e3']

   f.close() 
  print(f'::set-output name=istl_in_e1::{istl_in_e1}')



if __name__ == '__main__':
  main()