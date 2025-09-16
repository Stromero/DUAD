import pytest
import os

if __name__ == "__main__":
    script_dir = os.path.dirname(os.path.abspath(__file__))

    tests_path = os.path.join(script_dir,"tests")

    #exit_code = pytest.main(["-q", "--disable-warnings", "tests/"])
    exit_code = pytest.main(["-q", "--disable-warnings", "--tb=short", tests_path])
    if exit_code == 0:
        print("\n✅ Todos los tests pasaron correctamente")
    else:
        print("\n❌ Algunos tests fallaron. Revisa el log arriba.")