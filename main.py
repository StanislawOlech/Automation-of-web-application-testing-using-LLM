from specification_generator.gen_spec import generate_specification
from test_data_generator import generate_test_data
from website_generator.website import Website
from tester import test_website


def main():
    num_tests = 1000 # TODO chose a suitable number
    for test in range(num_tests):
        spec      = generate_specification()
        test_data = generate_test_data(spec)
        website   = Website(spec)
        score     = test_website(website, test_data)

        # TODO add metric collection
        print(f"Test {test+1}/{num_tests} completed.")


if __name__ == "__main__":
    main()