import capsolver

# Consider using environment variables for sensitive information
capsolver.api_key = "Your Capsolver API Key"
PAGE_URL = "https://www.sephora.com/"
PAGE_KEY = "6LdPdW0UAAAAAHNh5_q7pTCQS1lxzqmZ8-k3NDvb"

def solve_recaptcha_v2(url, key):
    try:
        solution = capsolver.solve({
            "type": "ReCaptchaV2TaskProxyless",
            "websiteURL": url,
            "websiteKey":key,
        })
        return solution
    except Exception as e:
        print(e)

def main():
    print("Solving reCaptcha v2")
    solution = solve_recaptcha_v2(PAGE_URL, PAGE_KEY)
    print("Solution: ", solution)

if __name__ == "__main__":
    main()
    